\version "2.24.4"
\header {
  title = "Symphony No. 9 Bass Chorus 237–"
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
    \set Score.currentBarNumber = #237
    R1 | r2 a4^\f a | R1 r2 a4^\f a |
  }
  \addlyrics {
    Freu -- de! Freu -- de!
  }
  >>
  \layout { indent = 0 }
  \midi {}
}
