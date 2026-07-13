# Vaccine Drug Checker (Impf-Medikamenten Check)

A simple, fast, and secure web application to check if a patient's medication is an immunosuppressant and how it affects live vaccinations (such as Yellow Fever). 

Based on the official DTG (Deutsche Gesellschaft für Tropenmedizin, Reisemedizin und Globale Gesundheit e.V.) guidelines for 2026.

## Features
- **Auto-complete Search**: Type in a generic substance or brand name (Handelsname) and instantly get matching results.
- **Safety Highlights**: Drugs that are known immunosuppressants are highlighted in a red warning card.
- **DTG Recommendations**: Instantly view whether a live vaccine is allowed, how long the therapy pause should be, and what the expected immune response for dead vaccines is.
- **Comprehensive Database**: Powered by the official WIdO ATC classification and Wikidata.

## Architecture
This is a Vanilla HTML/CSS/JS application. It requires no build tools, no servers, and no dependencies to run. 

### Running Locally
Just double click `index.html` to open it in your browser.

### Hosting
The `drug-checker-web-app` folder is ready to be deployed to **GitHub Pages**, Vercel, Netlify, or any static file server.

## Generating the Database
If you need to update the database in the future:
1. Go to the `data_generation/` directory.
2. Replace `ATC_GKV_AI_2026.xlsx` with the latest version from WIdO.
3. Run `python3 build_database.py` to merge the official DTG immunosuppressants (`drugs_germany.json`) with the new ATC list.
4. Run `python3 fetch_wikidata_brands.py` to enrich the database with open-source German brand names from Wikidata.
5. Copy the generated `app_drugs_db.json` to the `drug-checker-web-app/` folder.
