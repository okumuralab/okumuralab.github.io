\version "2.24.4"
\header {
  title = "Symphony No. 9 Bass Chorus 543–"
  composer = "Ludwig van Beethoven"
  tagline = ""
}
\language "english"
\score {
  <<
  \relative {
    \clef bass
    \key d \major
    \time 6/8
    \tempo "Allegro assai vivace" 2. = 84
    \set Score.currentBarNumber = #543
    \mark "M"
    d'4.^\f d | d d | a a | a b4( cs8) | d4. a | a a | a^\sf~a4 a8 | a4 r8 r4 r8 | \break
    d4. d | d d | g,^\sf g | g g | a a | a a | a^\sf~a4 a8 | d,4 r8 r4 r8 | \break
    a'4. a | a a | a a | a a | a a | as fs | b e, | a! a^\ff( | \break
    d) d | d d | g, g | g^\sf g | a a | a a | a~a4 a8 | d,4 r8 r4 r8 |
    a'4. a | a a | a a | a a | a a | as fs | b e, | a! a^\ff( |
    d) d | d d | g, g | g^\sf g | a a | a a | a~a4 a8 | d,4. r4 r8 |
  }
  \addlyrics {
    Freu -- de, schö -- ner Göt -- ter -- fun -- "ken __,"
    Toch -- ter aus E -- ly -- si -- um,
    Wir bet -- re -- ten feu -- er -- trun -- ken,
    Himm -- li -- sche, dein Hei -- lig -- tum!
    Dei -- ne Zau -- ber bin -- den wie -- der,
    Was die Mo -- de streng ge -- teilt;
    Al -- le Men -- schen wer -- den Brü -- der,
    Wo dein sanf -- ter Flü -- gel weilt.
    Dei -- ne Zau -- ber bin -- den wie -- der,
    Was die Mo -- de streng ge -- teilt;
    Al -- le Men -- schen wer -- den Brü -- der,
    Wo dein sanf -- ter Flü -- gel weilt.
  }
  >>
  \layout { indent = 0 }
  \midi {}
}
