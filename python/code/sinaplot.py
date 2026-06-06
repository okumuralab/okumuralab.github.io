import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

def sinaplot(x, y, data, violin=True, max_width=0.8, title=None,
             show_grid=False, ax=None, random_seed=None):
    """
    Draws a sinaplot: a jittered dot plot with optional violin shape background.

    Parameters:
    - x: str. Categorical column name in data.
    - y: str. Numerical column name in data.
    - data: pandas.DataFrame. Input data.
    - violin: bool. Whether to draw violin background. Default True.
    - max_width: float. Maximum horizontal jitter width. Default 0.8.
    - title: str or None. Plot title.
    - show_grid: bool. Whether to show grid.
    - ax: matplotlib.axes.Axes or None. Axes to plot into. If None, uses current Axes.
    - random_seed: int or None. Seed for reproducibility of jitter.

    Returns:
    - ax: The matplotlib Axes used.
    """
    if random_seed is not None:
        np.random.seed(random_seed)
    fig = plt.gcf()
    if ax is None:
        ax = plt.gca()
    data = data.dropna(subset=[x, y])
    categories = np.sort(data[x].unique())
    default_color = plt.rcParams['axes.prop_cycle'].by_key()['color'][0]

    def offset(category_index, data, scale=1.0):
        return np.array([category_index] * len(data)) + (scale * data)

    density_max = 0
    for category in categories:
        values = data[data[x] == category][y].values
        n = len(values)
        if n >= 2:
            kde = gaussian_kde(values)
            density_max = max(density_max, n * kde(values).max())

    for i, category in enumerate(categories):
        values = data[data[x] == category][y].values
        n = len(values)
        if n < 2:
            ax.scatter([i] * n, values, color=default_color, s=10, zorder=3)
            continue
        kde = gaussian_kde(values)
        if violin:
            value_range = np.linspace(values.min(), values.max(), 50)
            density = kde(value_range)
            density = n * density / density_max * max_width / 2
            ax.fill_betweenx(value_range, offset(i, density), offset(i, -density),
                             color=default_color, alpha=0.3, zorder=1)
        jitter = n * (np.random.random(n) * 2 - 1) * kde(values) / density_max * max_width / 2
        ax.scatter(offset(i, jitter), values, color=default_color, s=10, zorder=3)

    ax.set_xticks(range(len(categories)))
    ax.set_xticklabels(categories)
    ax.set_xlim(-0.8, len(categories) - 0.2)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    if title:
        ax.set_title(title)
    ax.grid(show_grid)
    return ax  # just in case
