\version "2.24.4"
\header {
  title = "Symphony No. 9 Bass Chorus 595–"
  composer = "Ludwig van Beethoven"
  tagline = ""
}
\language "english"
\score {
  <<
  \relative {
    \clef bass
    \key g \major
    \time 3/2
    \tempo "Andante maestoso" 2 = 72
    \set Score.currentBarNumber = #595
    g1^\ff g2 | fs-! d-! e'^\ff~ | e1 e2-! | d-! b-! r |
    c1 c2 | b-! g1 | e'1^\ff e2 | d1. |
    r2 g,2^\f b | d d, d~ | d c c' | b g r |
    a1^\sf a2 | b c1^\sf | c^\ff c2 | d1. |
    c2( d2.) c4 | r2 f2. f4 | f1 f2 | f1 r2 |
    d1^\sf c2 | c( a) g | f'1^\sf e2 \bar "||"
    \key f \major
    e-! d-! r2 | f,1~ f4 f | r a( bf2.) bf4 | bf1 bf2 | bf bf1~^\sf
    bf2 bf( c) | c1 c2 c2.( d4) e( f) | g,2 g r \bar "||" \break
    \key bf \major
    \tempo 2 = 60
    % \< \> \! \cresc
    % https://lilypond.org/doc/Documentation/notation/expressive-marks-attached-to-notes
    R1.*4 | <>\< \after 2 \> \after 1 \! g1~ g4 g |
    c,2-! c-! r | a~ a2. g4 | d'2-! d'-! r |
    g,1^\pp^\cresc  g2 | f1 f2 | bf, bf'\! r | c1^\ff r2 |
    c,1^\pp c2 | c'1^\cresc c2 c( f,) f' | d1.^\f |
    r2 ef!2.^\ff ef4 | ef1 ef2 | ef ef1 | ef^\sf ef2 | R1.*4 |
    r2 g,2.^\pp g4 | g1 g2 | g g1 | g g2\fermata \bar "||"
  }
  \addlyrics {
    Seid um -- schlun -- gen, Mil -- li -- o -- nen!
    Die -- sen Kuß der gan -- zen Welt!
    Seid um -- schlun -- gen, Mil -- - li -- o -- nen!
    Die -- sen Kuß der gan -- zen Welt!
    Brü -- der! ü -- berm Ster -- nen -- zelt
    Muß ein lie -- ber Va -- ter woh -- nen.
    Brü -- der! ü -- berm Ster -- nen -- zelt
    "Muß ___" "ein __" lie -- ber Va -- "ter __" woh -- nen.
    "Ihr ___" stürzt nie -- der, Mil -- li -- o -- nen?
    Ah -- nest du den Schöp -- fer, Welt?
    Such' ihn ü -- berm Ster -- nen -- zelt!
    Ü -- ber Ster -- nen muß er woh -- nen.
    Ü -- ber Ster -- nen muß er woh -- nen.
  }
  >>
  \layout { indent = 0 }
  \midi {}
}
