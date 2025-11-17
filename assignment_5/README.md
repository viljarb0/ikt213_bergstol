# Face Recognition Lab - Lab 5

Dette prosjektet implementerer ansiktsgjenkjenning ved hjelp av `face_recognition` biblioteket.

## Oppgave 1: Live Face Recognition (doorcam.py)

Kjør live ansiktsgjenkjenning fra webkamera:

```bash
python doorcam.py
```

### Kontroller:
- **`s`** - Ta skjermbilde (lagres i `screenshots/` mappen)
- **`q`** - Avslutt programmet

## Oppgave 2: Face Recognition med bilder

### Steg 1: Forbered bildene

1. **Opprett individuelle bilder:**
   - Ta et bilde av hvert gruppemedlem
   - Legg bildene i `known_people/` mappen
   - **Viktig:** Filnavnet skal være personens navn (f.eks. `John.jpg`, `Jane.png`)

2. **Opprett gruppebilde:**
   - Ta et gruppebilde med alle medlemmene
   - Legg bildet i `unknown_people/` mappen

### Steg 2: Kjør ansiktsgjenkjenning

Naviger til prosjektmappen og kjør:

```bash
face_recognition --show-distance true ./known_people ./unknown_people
```

Dette vil:
- Sammenligne ansiktene i gruppebildet med de kjente personene
- Vise ansiktsavstanden (face distance) for hvert match
- Skrive ut hvilke personer som ble gjenkjent i gruppebildet

### Eksempel output:
```
./unknown_people/group_photo.jpg,John,0.35
./unknown_people/group_photo.jpg,Jane,0.42
```

### Tolerance

Standard tolerance er 0.6. Du kan justere dette med `--tolerance` flagget:

```bash
face_recognition --show-distance true --tolerance 0.54 ./known_people ./unknown_people
```

## Installasjon

Se `requirements.txt` for alle nødvendige avhengigheter.

```bash
pip install -r requirements.txt
```

**Merk:** På Windows krever `dlib` CMake og Visual Studio Build Tools. Se `INSTALLASJON_DLIB.md` for detaljerte instruksjoner.

## Mappestruktur

```
face_recognition/
├── doorcam.py              # Live ansiktsgjenkjenning
├── requirements.txt        # Python avhengigheter
├── known_people/          # Individuelle bilder (filnavn = personens navn)
├── unknown_people/        # Gruppebilde
├── screenshots/           # Skjermbilder fra doorcam.py (generert)
└── known_faces.dat        # Lagret ansiktsdata (generert)
```
