from webtech import app, db
from webtech.models import Huisje

# De data lijst
huisjes_data = [
    (4, 550.20, "Mooi huisje aan de duinen"),
    (8, 950.00, "Luxe villa met sauna"),
    (6, 720.50, "Ruime gezinswoning"),
    (4, 495.00, "Gezellige bungalow"),
    (6, 680.00, "Moderne boswoning"),
    (8, 1100.00, "Groot landhuis met tuin"),
    (4, 525.45, "Knusse studio voor twee"),
    (6, 710.00, "Huisje met uitzicht op zee"),
    (8, 890.00, "Comfortabele groepsaccommodatie"),
    (4, 560.00, "Authentiek vissershuisje")
]

# ALLES wat met de database te maken heeft moet binnen dit blok:
with app.app_context():
    # Optioneel: Maak de tabellen aan als ze nog niet bestaan
    # db.create_all() 

    for p, prijs, tekst in huisjes_data:
        nieuw_huisje = Huisje(personen=p, weekprijs=prijs, beschrijving=tekst)
        db.session.add(nieuw_huisje)

    # Definitief opslaan
    db.session.commit()
    print("10 huisjes succesvol toegevoegd!")
