# Testing Skills

Mokomoji GitHub repozitorija, kurioje kuriami, tikrinami ir tobulinami DI įgūdžiai (*AI Skills*). Tikslas – mokytis praktiškai, mažais žingsniais ir kiekvieną įgūdį patikrinti prieš laikant jį baigtu.

## Struktūra

```text
skills/
├── skill-creator/            # Anthropic skill kūrimo ir testavimo pavyzdys
│   ├── SKILL.md
│   └── ...
└── miestu-oras/              # Mūsų pirmasis sukurtas įgūdis
    ├── SKILL.md
    └── scripts/
        └── weather.py
```

Kiekvienas naujas įgūdis kuriamas atskirame `skills/<skill-name>/` kataloge. Esamo `skill-creator` kodo nekeisti vien tam, kad būtų sukurtas kitas įgūdis.

## Reikalavimai kiekvienam naujam Skill

1. **Aiški užduotis.** Vienu ar dviem sakiniais aprašyti, kokią problemą įgūdis sprendžia, kada jį reikia naudoti ir kokio rezultato vartotojas tikisi.
2. **Tinkamas pavadinimas.** Katalogo ir įgūdžio pavadinime naudoti mažąsias lotyniškas raides, skaičius ir brūkšnelius, pvz., `miestu-oras`.
3. **Privalomas `SKILL.md`.** Jo pradžioje turi būti YAML antraštė su `name` ir `description`, po jos – aiškios vykdymo instrukcijos. `description` turi pasakyti ir *ką* įgūdis daro, ir *kada* jį naudoti.
4. **Tik būtini papildomi failai.** `scripts/` skirti vykdomam kodui, `references/` – dokumentacijai, `assets/` – šablonams ir kitam reikalingam turiniui. Tuščių ar nenaudojamų katalogų nekaupti.
5. **Patikimi duomenys.** Nurodyti šaltinius, atskirti faktus nuo prognozių ir niekada neišgalvoti trūkstamų duomenų. Išorinės API klaidas parodyti suprantamai.
6. **Saugumas.** Į GitHub nekelti slaptažodžių, API raktų, prisijungimo žetonų ar asmens duomenų be aiškaus pagrindo. Jei reikia prisijungimo duomenų, naudoti saugią aplinkos konfigūraciją.
7. **Testavimas.** Prieš įkeliant pakeitimus patikrinti sėkmingą scenarijų, nepilnus ar neteisingus duomenis ir išorinio šaltinio nepasiekiamumą. Jei naudojamas skriptas, bent kartą jį iš tikrųjų paleisti.
8. **Rezultato patikra.** Patikrinti `SKILL.md` antraštę, failų struktūrą, programos išvestį ir tai, kad GitHub esantys failai atitinka patikrintą versiją.
9. **Aiškus aprašymas lietuviškai.** Vartotojui paaiškinti, kas sukurta, kaip paleisti, kokie apribojimai ir kas patikrinta. Techninius terminus trumpai paaiškinti.
10. **Versijų kontrolė.** Pakeitimus įkelti su prasmingu *commit* pranešimu. Didesniems pakeitimams naudoti atskirą šaką ir *Pull Request*; netrinti kito darbo be suderinimo.

### Minimalus naujo įgūdžio šablonas

```markdown
---
name: mano-skill
description: Ką įgūdis atlieka ir kada jį naudoti.
---

# Mano Skill

1. Gauti reikalingus duomenis.
2. Patikrinti, ar jie teisingi ir pakankami.
3. Atlikti užduotį.
4. Pateikti aiškų rezultatą ir nurodyti ribotumus.
```

## Pirmasis įgūdis: `miestu-oras`

**Paskirtis:** iš oficialaus [Meteo.lt API](https://api.meteo.lt/) gauti artimiausią prognozuojamą oro temperatūrą ir sąlygas penkiems didžiausiems Lietuvos miestams.

**Miestai:** Vilnius, Kaunas, Klaipėda, Šiauliai, Panevėžys.

**Reikalaujamas rezultatas:** lentelė su miesto pavadinimu, temperatūra (°C), sąlygomis lietuviškai ir prognozės laiku Lietuvos laiko juostoje. Būtina nurodyti Meteo.lt kaip šaltinį ir pažymėti, kad tai **prognozė, ne faktinis šios minutės matavimas**.

**Paleidimas** (reikia Python 3 ir interneto ryšio):

```bash
python3 skills/miestu-oras/scripts/weather.py
```

Skriptas naudoja Python standartinę biblioteką, tad papildomų Python paketų diegti nereikia. Jei duomenų kuriam nors miestui nepavyksta gauti, vietoje išgalvotų reikšmių turi būti rodomas aiškus pranešimas.

## Kada darbas laikomas baigtu?

- [ ] Įgūdžio paskirtis ir naudojimo atvejai aprašyti.
- [ ] Yra tinkamas `SKILL.md` ir tik reikalingi papildomi failai.
- [ ] Pagrindinis veikimo scenarijus išbandytas.
- [ ] Išbandytas bent vienas klaidos ar trūkstamų duomenų scenarijus.
- [ ] Rezultate pateiktas šaltinis, laikas ir svarbūs apribojimai.
- [ ] Failai įkelti į GitHub ir patikrinti po įkėlimo.

> **Svarbu:** įgūdžio failai GitHub repozitorijoje savaime neįdiegia jo į ChatGPT ar kitą DI aplinką. Įdiegimo ir vykdymo būdas priklauso nuo konkretaus įrankio.

## Naudotas pavyzdys

`skills/skill-creator/` nukopijuotas iš [Anthropic skills repozitorijos](https://github.com/anthropics/skills/tree/main/skills/skill-creator). Tai mokomoji medžiaga ir įgūdžių kūrimo praktikų pavyzdys; originalo licencijos sąlygos pateiktos jo `LICENSE.txt` faile.
