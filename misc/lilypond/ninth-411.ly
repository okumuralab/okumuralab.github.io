\version "2.24.4"
\header {
  title = "Symphony No. 9 Bass Chorus 411–"
  composer = "Ludwig van Beethoven"
  tagline = ""
}
\language "english"
\score {
  <<
  \relative {
    \clef bass
    \key bf \major
    \time 6/8
    \tempo "Allegro assai vivace" 2. = 84
    \set Score.currentBarNumber = #411
    f4 r8 f4 r8 | f4. f | c c | ef( d4 c8) | bf'4. bf,4 r8 | af'4. af,4 r8 | \break
    g'4 r8 g4 f8 | ef4. e4 r8 | f4 r8 f4 r8 | f2.~ | f4. f | bf4( f8) f4 r8 | R2. |
    bf4.^\sf bf4 r8 | R2. | ef4.^\sf ef,4 r8 | f4. f | f2.^\sf~ | f4. f4. | f2.^\sf~ |
    \mark "K"
    f4. bf,4 r8 |
  }
  \addlyrics {
    Lau -- fet, Brü -- der, eu -- re "Bahn ___,"
    Freu -- dig, wie ein Held zum "__" Sie -- gen.
    wie ein "Held ___" zum Sie -- gen.
    freu -- dig, freu -- dig, wie ein "Held ___" zum Sie -- gen.
  }
  >>
  \layout { indent = 0 }
  \midi {}
}
