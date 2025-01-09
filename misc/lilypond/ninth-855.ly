\version "2.24.4"
\header {
  title = "Symphony No. 9 Bass Chorus 855–"
  composer = "Ludwig van Beethoven"
  tagline = ""
}
\language "english"
\score {
  <<
  \relative {
    \clef bass
    \key d \major
    \time 2/2
    \tempo "Presto" 2 = 132
    \set Score.currentBarNumber = #855
    d'4^\f d cs a | e' e ds b | e, fs g gs | a gs a r | \break
    r2 r4 gs | a gs a2~ | a1~ | a1~ | a1 | a4 a r2 |
    g4( a) g( fs) | g4( a) g( fs) | g4( a) g fs | g4( a) g( fs) |
    e2 d4 d | g2 g | a g | fs1 | e2 d4 d | g2 g | a a | d,4 d r2 |
    d'4 d cs a | R1 | e'4 e ds b | b2^\ff b | b b | b b | c c |
    c c | f d | a a | b^\ff b^\sf~ | b b | b b | b b | c^\ff c |
    c c | f^\ff d | a a4( c) | c2^\ff( b4 g) | e' cs! a g | e cs a a'~ | a2 a4( c) |
    c c b^\ff g | e' cs! a g | e cs a a'~ | a2 a | d, r |
    b'4 b r2 | g4 g e e | a2.^\ff a4 | a d, r2 | R1 | r2 a'4 a |
    a1^\ff~ | a2. a4 | a d, r2 | R1*2 | r2 a'2^\ff~ | \break
    \time 3/4
    \tempo "Maestoso" 4 = 60
    \autoBeamOff
    a4. a8 a8. a16^\p | a8. a16 a4 r | d8.^\f d16 g,4.^\sf a8 |
    a8.^\ff a16 a8 d, a'8. a16 | \break
    \time 2/2
    \tempo "Prestissimo" 1 = 88
    a2^\ff d,4 r |
  }
  \addlyrics {
    Seid um -- schlun -- gen Mil -- li -- o -- nen!
    Die -- sen Kuß der gan -- zen Welt!
    der gan -- zen "Welt _______________!"
    Brü -- der!
    ü -- "berm __" Ster -- nen -- "zelt __"
    Muß ein lie -- ber Va -- ter,
    ein lie -- ber Va -- ter woh - nen,
    ein lie -- ber Va -- ter woh -- nen.
    Seid um -- schlun -- gen! seid um -- schlun -- gen!
    Die -- sen Kuß der gan -- zen Welt, der gan -- zen Welt, der gan -- zen Welt!
    Die -- sen Kuß der gan -- zen Welt, der gan -- zen Welt, der gan -- "zen ___,"
    gan - - - - - - - - "zen __" Welt,
    der gan - - - - - - - - - zen Welt!
    Freu -- de, Freu -- de, schö -- ner Göt -- ter -- fun -- ken!
    schö -- ner Göt -- ter -- fun -- ken!
    Toch -- ter aus E -- ly -- si -- um!
    Freu -- de schö -- ner Göt -- ter -- fun -- ken!
    Göt -- ter -- fun -- ken!
  }
  >>
  \layout {
    indent = 0
    ragged-last = ##t
  }
  \midi {}
}
