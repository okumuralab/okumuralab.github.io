\version "2.24.4"
\header {
  title = "Symphony No. 9 Bass Chorus 795–"
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
    \tempo "Allegro ma non tanto" 2 = 120
    \set Score.currentBarNumber = #795
    \mark "S"
    e^\p^\cresc e d d | g g fs fs |
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
  \midi {}
}
