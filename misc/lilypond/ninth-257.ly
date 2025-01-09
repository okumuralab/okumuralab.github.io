\version "2.24.4"
\header {
  title = "Symphony No. 9 Bass Chorus 257–"
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
    \set Score.currentBarNumber = #257
    \mark "D"
    e^\f e fs d | e fs8( g) fs4 d | e fs8( g) fs4 e |
    d e a, fs'~ | fs fs g a | a g \autoBeamOff fs( g8) e \autoBeamOn |
    d4 d e fs | e4. d8 d2 |
  }
  \addlyrics {
    Dei -- ne Zau -- ber bin -- den wie -- der, Was die Mo -- de
    streng ge -- teilt; Al -- le Men -- schen wer -- den Brü -- der,
    Wo dein sanf -- ter Flü -- gel weilt.
  }
  >>
  \layout { indent = 0 }
  \midi {}
}
