# CASE: RailNL

## Doel van het project:
Het doel van het project is het oplossen van de case RailNL (voor meer informatie, zie: https://theorie.mprog.nl/cases/railnl). Kortgezegd is het uiteindelijke doel het verbinden van trein-lijnvoeringen. Meegegeven in de map 'data' zijn twee lijnvoeringen, de ene lijnvoering is kleiner, deze is de Hollands lijnvoering. De tweede lijnvoering is groter en is de Nationale lijnvoering. Dit is een optimalisatie project waarbij er in een periode van 4 weken tijd gezocht werd naar het vinden van een zo goed mogelijk algoritme.

Binnen een gegeven tijdsframe worden een aantal trajecten verbonden. Een traject is een route van sporen en stations waarover treinen heen en weer rijden. Met de meegegeven doelfunctie wordt berekent hoe goed de trajecten scoren.

## Vereisten
Dit project vereist geen externe packages.

## Gebruiksaanwijzing
Om een oplossing te verkrijgen voor de gewenste lijnvoering, moet main.py gerund worden. Deze file zal de gebruiker vragen welke algoritmes er gerund moeten worden. Main.py runt het gewenste algoritme 1000 keer, zodat er op die manier hoogstwaarschijnlijk een goede oplossing verschijnt. Vervolgens zal er een output verschijnen met de naam: 'output.csv' in de data map. 

    python3 main.py
    
## Structuur
De hierop volgende lijst beschrijft de mappen en files 
in het project, en waar je ze kan vinden:
* **/codes:** 
    * code voor de algoritmes
    * code voor de classes
* **/data:**
    * data bestanden die nodig zijn om de connecties tussen steden te maken
* **/results:**
    * map waarin de output wordt gegenereerd


## Auteurs
* Amber Cok
* Josje Veugen
* Julia van Tol
