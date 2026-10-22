---
name: miestu-oras
description: Gauti penkių didžiausių Lietuvos miestų (Vilniaus, Kauno, Klaipėdos, Šiaulių ir Panevėžio) artimiausią oro temperatūros bei orų sąlygų prognozę iš oficialios Meteo.lt API. Naudoti, kai vartotojas klausia apie šių miestų orus, temperatūrą arba prašo penkių didžiausių Lietuvos miestų orų suvestinės.
---

# Miestų oras

Pateikti Vilniaus, Kauno, Klaipėdos, Šiaulių ir Panevėžio oro temperatūrą ir sąlygas lietuviškai.

## Darbo eiga

1. Paleisti `python3 scripts/weather.py` iš šio įgūdžio katalogo. Skriptas naudoja tik Python standartinę biblioteką ir oficialią `https://api.meteo.lt/v1/` API.
2. Vartotojui pateikti skripto sugeneruotą lentelę, jos prognozės laiką ir šaltinio nuorodą. Aiškiai vadinti duomenis **prognoze**, o ne realaus laiko matavimais.
3. Jei skriptas nepasiekiamas vykdymo aplinkoje, patikrinti oficialios Meteo.lt API `GET /places/{place-code}/forecasts/long-term` penkioms vietovėms: `vilnius`, `kaunas`, `klaipeda`, `siauliai`, `panevezys`. Kiekvienam miestui imti artimiausią ne ankstesnę už esamą UTC laiką prognozės laiko žymą (`forecastTimeUtc`), laukus `airTemperature` ir `conditionCode`; kodus išversti į lietuvių kalbą. Nespėlioti duomenų.
4. Jei dalies miestų duomenys negaunami, tai aiškiai nurodyti. Jei negaunami visi, paaiškinti, kad šiuo metu prognozės pateikti negalima. Neišgalvoti temperatūrų.

## Svarbios ribos

- Šaltinis: [Lietuvos hidrometeorologijos tarnybos API](https://api.meteo.lt/).
- API `long-term` pateikia prognozę, o ne tiesioginį meteorologinės stoties matavimą.
- Laikai API pateikiami UTC; vartotojui rodyti Lietuvos laiką (`Europe/Vilnius`).
- Nepridėti kitų miestų ar papildomų rodiklių, nebent vartotojas paprašo.
