"""Permutation test and confidence intervals for the Brunner-Munzel effect.

The effect is

    P(X < Y) + 0.5 P(X = Y)

Use bm_permutation_test() as the main entry point.  Exact enumeration is used
when the number of permutations is small enough; otherwise Monte Carlo
permutations are used.  Small-range integer data are automatically accelerated
with bincount-based count tables.
"""

from __future__ import annotations

import itertools
import math
from dataclasses import dataclass

import numpy as np
from scipy.stats import t as student_t

__all__ = ["BMResult", "bm_effect", "bm_permutation_test"]


@dataclass(frozen=True)
class BMResult:
    """Result returned by bm_permutation_test()."""

    effect: float
    standard_error: float
    degrees_freedom: float
    p_value: float
    ci_low: float
    ci_high: float
    asymptotic_ci_low: float
    asymptotic_ci_high: float
    permutation_ci_low: float
    permutation_ci_high: float
    ci_level: float
    exact: bool
    permutations: int
    total_permutations: int
    method: str
    count_allocations: int | None = None


@dataclass(frozen=True)
class _CountData:
    x_counts: np.ndarray
    y_counts: np.ndarray
    total_counts: np.ndarray
    offset: int
    allocation_count: int | None


def _as_1d_float_array(values: np.ndarray | list[float], name: str) -> np.ndarray:
    arr = np.asarray(values, dtype=float)
    if arr.ndim != 1:
        raise ValueError(f"{name} must be one-dimensional")
    if len(arr) == 0:
        raise ValueError(f"{name} must not be empty")
    if not np.all(np.isfinite(arr)):
        raise ValueError(f"{name} must contain only finite values")
    return arr


def _midranks(values: np.ndarray) -> np.ndarray:
    """Return 1-based average ranks, with ties receiving their midrank."""
    order = np.argsort(values, kind="mergesort")
    sorted_values = values[order]
    ranks = np.empty(len(values), dtype=float)

    start = 0
    while start < len(values):
        stop = start + 1
        while stop < len(values) and sorted_values[stop] == sorted_values[start]:
            stop += 1
        # 1-based ranks from start + 1 through stop, averaged.
        ranks[order[start:stop]] = (start + 1 + stop) / 2
        start = stop

    return ranks


def _integer_count_data(
    x: np.ndarray,
    y: np.ndarray,
    *,
    max_count_range: int,
    compute_allocation_count: bool,
) -> _CountData | None:
    """Return bincount-friendly integer counts, or None when not suitable."""
    values = np.concatenate([x, y])
    if not np.all(values == np.floor(values)):
        return None

    min_value = int(np.min(values))
    max_value = int(np.max(values))
    count_range = max_value - min_value + 1
    if count_range > max_count_range:
        return None

    x_shifted = x.astype(np.int64) - min_value
    y_shifted = y.astype(np.int64) - min_value
    x_counts = np.bincount(x_shifted, minlength=count_range).astype(np.int64)
    y_counts = np.bincount(y_shifted, minlength=count_range).astype(np.int64)
    total_counts = x_counts + y_counts
    allocation_count = (
        _count_allocations(total_counts, int(np.sum(x_counts)))
        if compute_allocation_count
        else None
    )
    return _CountData(
        x_counts=x_counts,
        y_counts=y_counts,
        total_counts=total_counts,
        offset=min_value,
        allocation_count=allocation_count,
    )


def _resolve_method(
    x: np.ndarray,
    y: np.ndarray,
    *,
    method: str,
    max_count_range: int,
    compute_allocation_count: bool = False,
) -> tuple[str, _CountData | None]:
    if method not in {"auto", "rank", "count"}:
        raise ValueError("method must be 'auto', 'rank', or 'count'")

    count_data = _integer_count_data(
        x,
        y,
        max_count_range=max_count_range,
        compute_allocation_count=compute_allocation_count,
    )
    if method == "count":
        if count_data is None:
            raise ValueError(
                "method='count' requires integer-valued data with "
                f"max(value)-min(value)+1 <= {max_count_range}"
            )
        return "count", count_data
    if method == "auto" and count_data is not None:
        return "count", count_data
    return "rank", None


def bm_effect(
    x: np.ndarray | list[float],
    y: np.ndarray | list[float],
    *,
    method: str = "auto",
    max_count_range: int = 10_000,
) -> float:
    """Compute P(X < Y) + 0.5 P(X = Y).

    Integer-valued data with a small range automatically use a bincount-based
    implementation.  Other data use midranks in O((N + M) log(N + M)).
    """
    x = _as_1d_float_array(x, "x")
    y = _as_1d_float_array(y, "y")
    resolved_method, count_data = _resolve_method(
        x,
        y,
        method=method,
        max_count_range=max_count_range,
        compute_allocation_count=False,
    )
    if resolved_method == "count":
        assert count_data is not None
        return _bm_components_from_counts(count_data.x_counts, count_data.y_counts)[0]

    n = len(x)
    m = len(y)

    pooled = np.concatenate([x, y])
    x_rank_sum = float(np.sum(_midranks(pooled)[:n]))
    # Mann-Whitney U for P(X > Y) + 0.5 P(X = Y), then reverse orientation.
    u_x = x_rank_sum - n * (n + 1) / 2
    return float(1 - u_x / (n * m))


def _weighted_sample_variance(
    values: np.ndarray,
    weights: np.ndarray,
    *,
    mean: float,
    ddof: int = 1,
) -> float:
    total_weight = int(np.sum(weights))
    if total_weight <= ddof:
        return 0.0
    return float(np.sum(weights * (values - mean) ** 2) / (total_weight - ddof))


def _welch_satterthwaite_df(
    var_x: float,
    n: int,
    var_y: float,
    m: int,
) -> float:
    term_x = var_x / n
    term_y = var_y / m
    denominator = 0.0
    if n > 1:
        denominator += term_x * term_x / (n - 1)
    if m > 1:
        denominator += term_y * term_y / (m - 1)
    if denominator == 0:
        return math.nan
    return (term_x + term_y) ** 2 / denominator


def _confidence_interval(
    effect: float,
    standard_error: float,
    critical_value: float,
    *,
    clip: bool,
) -> tuple[float, float]:
    if standard_error == 0 or not np.isfinite(critical_value):
        return effect, effect
    low = effect - critical_value * standard_error
    high = effect + critical_value * standard_error
    if clip:
        low = max(0.0, low)
        high = min(1.0, high)
    return low, high


def _asymptotic_ci(
    effect: float,
    standard_error: float,
    degrees_freedom: float,
    alpha: float,
) -> tuple[float, float]:
    critical_value = float(student_t.ppf(1 - alpha / 2, degrees_freedom))
    return _confidence_interval(
        effect,
        standard_error,
        critical_value,
        clip=False,
    )


def _bm_components_from_counts(
    x_counts: np.ndarray,
    y_counts: np.ndarray,
) -> tuple[float, float, float]:
    """Return the effect, standard error, and df from integer value counts."""
    n = int(np.sum(x_counts))
    m = int(np.sum(y_counts))
    if n == 0 or m == 0:
        raise ValueError("both x and y must contain at least one value")

    y_cumsum = np.cumsum(y_counts)
    y_greater = m - y_cumsum
    h_x = (y_greater + 0.5 * y_counts) / m
    effect = float(np.sum(x_counts * h_x) / n)

    x_less = np.cumsum(x_counts) - x_counts
    h_y = (x_less + 0.5 * x_counts) / n

    var_x = _weighted_sample_variance(h_x, x_counts, mean=effect)
    var_y = _weighted_sample_variance(h_y, y_counts, mean=effect)
    standard_error = math.sqrt(var_x / n + var_y / m)
    degrees_freedom = _welch_satterthwaite_df(var_x, n, var_y, m)
    return effect, standard_error, degrees_freedom


def _bm_components(x: np.ndarray, y: np.ndarray) -> tuple[float, float, float]:
    """Return the effect, Brunner-Munzel standard error, and df."""
    n = len(x)
    m = len(y)
    effect = bm_effect(x, y)

    y_sorted = np.sort(y)
    y_left = np.searchsorted(y_sorted, x, side="left")
    y_right = np.searchsorted(y_sorted, x, side="right")
    h_x = (m - y_right + 0.5 * (y_right - y_left)) / m

    x_sorted = np.sort(x)
    x_left = np.searchsorted(x_sorted, y, side="left")
    x_right = np.searchsorted(x_sorted, y, side="right")
    h_y = (x_left + 0.5 * (x_right - x_left)) / n

    var_x = np.var(h_x, ddof=1) if n > 1 else 0.0
    var_y = np.var(h_y, ddof=1) if m > 1 else 0.0
    standard_error = math.sqrt(var_x / n + var_y / m)
    degrees_freedom = _welch_satterthwaite_df(var_x, n, var_y, m)
    return effect, standard_error, degrees_freedom


def _split_components(values: np.ndarray, x_indices: np.ndarray) -> tuple[float, float]:
    mask = np.zeros(len(values), dtype=bool)
    mask[x_indices] = True
    effect, standard_error, _ = _bm_components(values[mask], values[~mask])
    return effect, standard_error


def _split_count_components(
    total_counts: np.ndarray,
    x_counts: np.ndarray,
) -> tuple[float, float]:
    effect, standard_error, _ = _bm_components_from_counts(
        x_counts,
        total_counts - x_counts,
    )
    return effect, standard_error


def _t_stat(effect: float, standard_error: float, null_effect: float = 0.5) -> float:
    if standard_error == 0:
        return 0.0 if effect == null_effect else math.copysign(math.inf, effect - null_effect)
    return (effect - null_effect) / standard_error


def _quantile_higher(values: np.ndarray, probability: float) -> float:
    """Small helper equivalent to NumPy's 'higher' quantile method."""
    if len(values) == 0:
        return math.nan
    sorted_values = np.sort(values)
    index = int(math.ceil(probability * len(sorted_values))) - 1
    index = min(max(index, 0), len(sorted_values) - 1)
    return float(sorted_values[index])


def _weighted_quantile_higher(
    values: np.ndarray,
    weights: np.ndarray,
    probability: float,
) -> float:
    if len(values) == 0:
        return math.nan
    order = np.argsort(values)
    sorted_values = values[order]
    sorted_weights = weights[order]
    cutoff = int(math.ceil(probability * int(np.sum(sorted_weights))))
    cutoff = max(cutoff, 1)
    index = int(np.searchsorted(np.cumsum(sorted_weights), cutoff, side="left"))
    return float(sorted_values[min(index, len(sorted_values) - 1)])


def _count_allocations(total_counts: np.ndarray, n: int) -> int:
    """Count unique integer allocations x_counts with sum n."""
    dp = np.zeros(n + 1, dtype=object)
    dp[0] = 1
    for count in total_counts:
        next_dp = np.zeros(n + 1, dtype=object)
        count = int(count)
        for used in range(n + 1):
            ways = dp[used]
            if ways == 0:
                continue
            max_take = min(count, n - used)
            for take in range(max_take + 1):
                next_dp[used + take] += ways
        dp = next_dp
    return int(dp[n])


def _iter_count_allocations(total_counts: np.ndarray, n: int):
    """Yield (x_counts, weight) for each unique count allocation."""
    total_counts = np.asarray(total_counts, dtype=np.int64)
    current = np.zeros(len(total_counts), dtype=np.int64)
    suffix_capacity = np.concatenate(([int(np.sum(total_counts))], np.cumsum(total_counts[::-1])[-2::-1]))

    def rec(pos: int, remaining: int, weight: int):
        if pos == len(total_counts) - 1:
            if 0 <= remaining <= total_counts[pos]:
                current[pos] = remaining
                yield current.copy(), weight * math.comb(int(total_counts[pos]), remaining)
            return

        rest_capacity = int(suffix_capacity[pos + 1])
        low = max(0, remaining - rest_capacity)
        high = min(int(total_counts[pos]), remaining)
        for take in range(low, high + 1):
            current[pos] = take
            yield from rec(
                pos + 1,
                remaining - take,
                weight * math.comb(int(total_counts[pos]), take),
            )

    yield from rec(0, n, 1)


def _random_count_allocation(
    rng: np.random.Generator,
    total_counts: np.ndarray,
    n: int,
) -> np.ndarray:
    if hasattr(rng, "multivariate_hypergeometric"):
        return rng.multivariate_hypergeometric(total_counts, n).astype(np.int64)

    expanded = np.repeat(np.arange(len(total_counts)), total_counts)
    sample = rng.choice(expanded, size=n, replace=False)
    return np.bincount(sample, minlength=len(total_counts)).astype(np.int64)


def bm_permutation_test(
    x: np.ndarray | list[float],
    y: np.ndarray | list[float],
    *,
    alpha: float = 0.05,
    n_resamples: int = 99_999,
    max_exact: int = 200_000,
    seed: int | None = None,
    method: str = "auto",
    max_count_range: int = 10_000,
) -> BMResult:
    """Permutation test for effect=0.5 plus two confidence intervals.

    The p-value uses the absolute studentized Brunner-Munzel statistic.
    The returned result includes both:

    * an asymptotic Brunner-Munzel t confidence interval, matching the usual
      lawstat/brunnermunzel calculation; and
    * a studentized permutation confidence interval, formed as

        observed_effect +/- q_(1-alpha) * observed_standard_error

    where q is taken from the permutation distribution of
    abs((permuted_effect - 0.5) / permuted_standard_error).
    """
    if not 0 < alpha < 1:
        raise ValueError("alpha must be between 0 and 1")

    x = _as_1d_float_array(x, "x")
    y = _as_1d_float_array(y, "y")
    n = len(x)
    m = len(y)
    values = np.concatenate([x, y])
    k = len(values)
    total_permutations = math.comb(k, n)
    resolved_method, count_data = _resolve_method(
        x,
        y,
        method=method,
        max_count_range=max_count_range,
        compute_allocation_count=True,
    )

    if resolved_method == "count":
        assert count_data is not None
        observed_effect, observed_se, observed_df = _bm_components_from_counts(
            count_data.x_counts,
            count_data.y_counts,
        )
    else:
        observed_effect, observed_se, observed_df = _bm_components(x, y)
    observed_abs_t = abs(_t_stat(observed_effect, observed_se))
    asymptotic_ci_low, asymptotic_ci_high = _asymptotic_ci(
        observed_effect,
        observed_se,
        observed_df,
        alpha,
    )

    if resolved_method == "count":
        assert count_data is not None
        assert count_data.allocation_count is not None
        exact = count_data.allocation_count <= max_exact
    else:
        exact = total_permutations <= max_exact

    if exact and resolved_method == "count":
        assert count_data is not None
        assert count_data.allocation_count is not None
        abs_t_values = np.empty(count_data.allocation_count, dtype=float)
        weights = np.empty(count_data.allocation_count, dtype=object)
        weighted_exceedances = 0
        for pos, (x_counts, weight) in enumerate(
            _iter_count_allocations(count_data.total_counts, n)
        ):
            effect, se = _split_count_components(count_data.total_counts, x_counts)
            abs_t = abs(_t_stat(effect, se))
            abs_t_values[pos] = abs_t
            weights[pos] = weight
            if abs_t >= observed_abs_t:
                weighted_exceedances += weight
        p_value = float(weighted_exceedances / total_permutations)
        used_permutations = count_data.allocation_count
        q = _weighted_quantile_higher(abs_t_values, weights, 1 - alpha)
    elif exact:
        abs_t_values = np.empty(total_permutations, dtype=float)
        for pos, combo in enumerate(itertools.combinations(range(k), n)):
            effect, se = _split_components(values, np.fromiter(combo, dtype=int))
            abs_t_values[pos] = abs(_t_stat(effect, se))
        p_value = float(np.mean(abs_t_values >= observed_abs_t))
        used_permutations = total_permutations
        q = _quantile_higher(abs_t_values, 1 - alpha)
    elif resolved_method == "count":
        assert count_data is not None
        rng = np.random.default_rng(seed)
        abs_t_values = np.empty(n_resamples, dtype=float)
        exceedances = 0
        for pos in range(n_resamples):
            x_counts = _random_count_allocation(rng, count_data.total_counts, n)
            effect, se = _split_count_components(count_data.total_counts, x_counts)
            abs_t = abs(_t_stat(effect, se))
            abs_t_values[pos] = abs_t
            if abs_t >= observed_abs_t:
                exceedances += 1
        p_value = (exceedances + 1) / (n_resamples + 1)
        used_permutations = n_resamples
        q = float(np.quantile(abs_t_values, 1 - alpha))
    else:
        rng = np.random.default_rng(seed)
        abs_t_values = np.empty(n_resamples, dtype=float)
        exceedances = 0
        for pos in range(n_resamples):
            indices = rng.choice(k, size=n, replace=False)
            effect, se = _split_components(values, indices)
            abs_t = abs(_t_stat(effect, se))
            abs_t_values[pos] = abs_t
            if abs_t >= observed_abs_t:
                exceedances += 1
        # Add-one correction keeps Monte Carlo p-values away from exactly zero.
        p_value = (exceedances + 1) / (n_resamples + 1)
        used_permutations = n_resamples
        q = float(np.quantile(abs_t_values, 1 - alpha))

    permutation_ci_low, permutation_ci_high = _confidence_interval(
        observed_effect,
        observed_se,
        q,
        clip=True,
    )

    return BMResult(
        effect=observed_effect,
        standard_error=observed_se,
        degrees_freedom=observed_df,
        p_value=p_value,
        asymptotic_ci_low=asymptotic_ci_low,
        asymptotic_ci_high=asymptotic_ci_high,
        permutation_ci_low=permutation_ci_low,
        permutation_ci_high=permutation_ci_high,
        ci_level=1 - alpha,
        exact=exact,
        permutations=used_permutations,
        total_permutations=total_permutations,
        method=resolved_method,
        count_allocations=(
            count_data.allocation_count if count_data is not None else None
        ),
    )
