\version "2.24.4"
\header {
  title = "Symphony No. 9 Bass Chorus 313–"
  composer = "Ludwig van Beethoven"
  tagline = ""
}
\language "english"
\score {
  <<
  \relative {
    \clef bass
    \key d \major
    \time 4/4
    \tempo "Allegro assai" 2 = 80
    \set Score.currentBarNumber = #313
    \mark "G"
    a a a a | a a a a | a a, a a | a a a a |
    d d d d | d d d d | d d d'4.^\sf d8 | d( a4) d8 d2 |
    d-! d-! | g,-! g-! | a-! a-! | d1 | e,2 e | a1^\ff |
    r2 e | a1^\ff | r2 a | f1^\ff\fermata \bar "||"
  }
  \addlyrics {
    Küs -- se gab sie uns und Re -- ben,
    Ei -- nen Freund, ge -- prüft im Tod;
    Wol - lust ward dem Wurm ge -- ge -- ben,
    Und der Che -- rub steht vor Gott,
    und der Che -- rub steht vor Gott,
    steht vor Gott, vor Gott, vor Gott.
  }
  >>
  \layout { indent = 0 }
  \midi {}
}
