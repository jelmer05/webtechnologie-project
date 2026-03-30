from webtech import app, db
from webtech.models import Huisje

# We maken een dictionary om de afbeeldingen te koppelen aan het aantal personen
afbeeldingen = {
    4: "https://s3.eu-west-1.amazonaws.com/v2-eu-ireland.bijzonderplekje.nl/wp-content/uploads/2018/04/13120727/HaagseStrandhuisjes_huisje_voorzijde-768x509.jpg",
    6: "https://images.origineelovernachten.nl/_upload/accommodation/1317/3e2e1c9a-d72b-47c4-82e9-df17d65644b2.jpg?w=1500&h=1125&mode=crop",
    8: "https://images.origineelovernachten.nl/_upload/accommodation/917/abf857ca-8ea8-4876-a3fd-94a3667890b8.JPG?w=1500&h=1125&mode=crop"
}

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

with app.app_context():
    # 1. Verwijder alle bestaande huisjes
    print("Oude huisjes aan het verwijderen...")
    Huisje.query.delete()
    
    # 2. Voeg de nieuwe huisjes toe
    for p, prijs, tekst in huisjes_data:
        # We pakken de juiste URL uit onze 'afbeeldingen' dictionary op basis van 'p'
        url = afbeeldingen.get(p)
        
        nieuw_huisje = Huisje(
            personen=p, 
            weekprijs=prijs, 
            beschrijving=tekst,
            afbeelding=url  # Zorg dat deze kolomnaam in je models.py staat!
        )
        db.session.add(nieuw_huisje)

    # 3. Opslaan
    db.session.commit()
    print("Database succesvol ververst met 10 nieuwe huisjes!")
