\version "2.24.4"
\header {
  title = "Symphony No. 9 Bass Chorus"
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
}
\markup { \column { \vspace #0.1 } }
\score {
  <<
  \relative {
    \clef bass
    \key d \major
    \time 4/4
    \tempo "Allegro assai" 2 = 80
    \set Score.currentBarNumber = #257
    \mark "D"
    e4^\f e fs d | e fs8( g) fs4 d | e fs8( g) fs4 e |
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
}
\markup { \column { \vspace #0.1 } }
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
    a4~^\f | a a, a' a | a a, a' a | a a as fs | b e, a! a,( |
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
}
\markup { \column { \vspace #0.1 } }
\score {
  <<
  \relative {
    \clef bass
    \key d \major
    \time 4/4
    \tempo "Allegro assai" 2 = 80
    \set Score.currentBarNumber = #313
    \mark "G"
    a4 a a a | a a a a | a a, a a | a a a a |
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
}
\markup { \column { \vspace #0.1 } }
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
}
\markup { \column { \vspace #0.1 } }
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
}
\markup { \column { \vspace #0.1 } }
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
}
\markup { \column { \vspace #0.1 } }
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
}
\markup { \column { \vspace #0.1 } }
\score {
  <<
  \relative {
    \clef bass
    \key d \major
    \time 4/4
    \tempo "Allegro ma non tanto" 2 = 120
    \set Score.currentBarNumber = #795
    \mark "S"
    e4^\p^\cresc e d d | g g fs fs |
    fs( e) d( a') | a( g) g( fs) |
    fs( e) d( a') | a( g) g( fs) | \break
    a^\f a, b a | d cs fs e | a g g r | R1*2 |
    r4 d'4~^\ff d4. d8 | d4 b b4. b8 | b4 g g4. g8 | g4 e e'4. e8 | \break
    \set Score.tempoHideNote = ##t
    \tempo "poco adagio" 2 = 40
    a,4-> a^\p a^\cresc a | b->\! b^\p b b | g2. g4 | a a a2~ | \break
    \tempo "Tempo I" 2 = 120
    a2 r2 | R1*3 | a4^\p^\cresc a a a | a a a a | a2 a | a a |
    a4^\f a, b a | d cs fs e | a g g r | R1*2 |
    r4 d'^\ff~ d4. d8 | d4 b b4. b8 | b4 g g4. g8 | g4 e r2 | r2 e'4. e8 |
    \tempo "poco adagio" 2 = 40
    e4 e,4 r2 |
    \set Score.tempoHideNote = ##f
  }
  \addlyrics {
    Dei -- ne Zau -- ber, Dei -- ne Zau -- ber
    bin -- den wie -- der, bin -- den wie -- der,
    Was die Mo -- de streng - - - - ge -- teilt;
    Al -- le Men -- schen, al -- le Men -- schen,
    al -- le Men -- schen, al -- le Men -- schen
    wer -- den Brü -- der,
    Wo dein sanf -- ter Flü -- gel "weilt __."
    Dei -- ne Zau -- ber, Dei -- ne Zau -- ber
    bin -- den wie -- der,
    Was die Mo -- de streng - - - - ge -- teilt;
    Al -- le Men -- schen, al -- le Men -- schen,
    al -- le Men -- schen, al -- le Men -- schen!
  }
  >>
  \layout { indent = 0 }
}
% \markup { \column { \vspace #0.1 } }
\pageBreak
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
}
