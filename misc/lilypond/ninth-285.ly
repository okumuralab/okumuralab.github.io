\version "2.24.4"
\header {
  title = "Symphony No. 9 Bass Chorus 285–"
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
    \set Score.currentBarNumber = #285
    \set Score.barNumberVisibility = #all-bar-numbers-visible
    \partial 4
    a~^\f | a a, a' a | a a, a' a | a a as fs | b e, a! a,( |
    d) d d^\sf cs8( b) | a( b) cs(^\dim d) e( fs) g( e) | fs4^\p fs d d | a' a, d2 |
  }
  \addlyrics {
    "Ja____," wer auch nur ei -- ne See -- le
    Sein nennt auf dem Er -- den -- rund!
    Und __ wer's nie ge -- konnt, der steh -- le __
    Wei -- nend sich aus die -- sem Bund!
  }
  >>
  \layout { indent = 0 }
  \midi {}
}
