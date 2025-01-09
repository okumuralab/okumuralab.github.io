\version "2.24.4"
\header {
  title = "Symphony No. 9 Bass Chorus 663–"
  composer = "Ludwig van Beethoven"
  tagline = ""
}
\language "english"
peup = \markup { \italic "più" \dynamic "p" }
\score {
  <<
  \relative {
    \clef bass
    \key d \major
    \time 6/4
    \tempo "Allegro energico e sempre ben marcato" 2. = 84
    \set Score.currentBarNumber = #663
    cs'2^\f cs4 d2 e4 | e2 d4 cs2 b4 | a2 a4 b2 cs4 | cs2 b4 a2( g4) |
    fs2 fs4 gs2 a4 | a2 g!4 fs2 e4 | d2 cs4 b2 a4 | d2 d4 d2 d'4^\ff~ |
    d2. d2. | cs2. a2. | b2. b2. | a2. fs2. | g2. g2. | fs2. d2. | b'2. b2. |
    a2 cs4~ cs2 b4 | a2. b2 cs4 | e,1.~ | e2 d4 d'2 a4~ | a1. |
    b2. e,2. | fs2 e'4 d2 cs4 | b4( a2) a2. | as2. fs2. | e'2. e2. | ds2. r2. |
    b2. b2. | b2. e,2. | d'!2. cs2. | d2. r2. |
    R1. | a2 a4 r2. | R1. | d2 a4 r2. | r2. e2 e4 | 
    b2 b4 cs2( d4) | e2 fs4 gs2 e4 | b'2 a4 b2( cs4) |
    R1. | r2. b2.~ | b2. b2. | as2. fs2. | d'2. b2. | cs2. cs2. |
    fs,2. fs2. | b2. r2. | d,2 d4 e2 fs4 | fs2 e4 d2 cs4 |
    cs2 cs4 ds2 e4 | fs2 ds4 cs2( b4) | fs'2 fs4 gs2 a!4 | a2 gs4 fs2 e4 |
    b'2 b4 e2 d4 | d2( cs4 b2) cs4 | b2( a4) r2. | R1. |
    r2. d2.~^\ff | d2. d2. | cs2. a2. | b2. b2. a2. fs2. |
    g2. g2. fs2. d'2. | e2. e2. e1.~ | e2. e2. | d1. |
    fs,2^\p r4 r4 r4 fs4 | c2 r4 r4 r4 c4 | a'2 r4 r4 r4 a4 | bf2 r4 r4 r4 bf4 |
    R1.*8 | bf,2 r4 r4 r4 bf4 | g'2 r4 r4 r4 g4 | gs2 r4 r4 r4 gs4 |
    a2.^\f a2.~^\sf | a2. a2. | R1. | a2.^\f a2. |
    r2. a2.~^\p | a2. a2. | a1.~^\< | a2. a2.\! | a2.-> a2.~^\p |
    a2. a2. | a2. a2. | a2. a2. | a2. a2. | a2.^\<( d,2.^\>) |
    g2.^\p g2. | g2.^\peup g2.  g1.~ | g2. g2.^\pp\fermata \bar "||"
  }
  \addlyrics {
    Freu -- de, schö -- ner Göt -- ter -- fun -- ken,
    Toch -- ter aus E -- ly -- si -- um,
    Wir bet -- re -- ten feu -- er -- trun -- ken,
    Himm -- li -- sche, dein Hei -- lig -- tum!
    Seid um -- schlun -- gen, Mil -- li -- o -- nen!
    Die -- sen Kuß der gan -- zen Welt - - - - - - - - - - - - - - -
    die -- sen Kuß der gan -- zen Welt,
    die -- sen Kuß der gan -- zen Welt!
    Freu -- de, Freu -- de,
    Wir bet -- re -- ten, "dein __" Hei - - - - lig -- "tum __."
    Seid um -- schlun -- gen!
    Die -- sen Kuß der gan -- zen Welt!
    Freu -- de, schö -- ner Göt -- ter -- fun -- ken,
    Toch -- ter aus E -- ly -- si -- um,
    Wir bet -- re -- ten feu -- er -- trun -- ken,
    Himm -- li -- sche, dein Hei -- lig -- "tum __."
    Seid um -- schlun -- gen, Mil -- li -- o -- nen!
    Die -- sen Kuß der gan -- zen, gan -- zen Welt!
    Ihr stürzt nie -- der, Mil -- li -- o -- nen?
    Such' ihn ü -- berm Ster -- nen -- zelt!
    Brü -- der, Brü -- der,
    ü -- berm Ster -- nen -- zelt
    Muß ein lie -- ber Va -- ter woh -- nen,
    "ein ___" lie -- ber Va -- ter woh -- nen.
  }
  >>
  \layout { indent = 0 }
  \midi {}
}
