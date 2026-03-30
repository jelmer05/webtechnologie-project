from webtech import app, db
from webtech.models import Huisje, Boeking, User

with app.app_context():
    # 1. Verwijder eerst alle oude boekingen (om dubbelingen te voorkomen)
    print("Oude boekingen verwijderen...")
    Boeking.query.delete()

    # 2. Zoek het huisje waar we de boekingen aan willen koppelen
    # We pakken gewoon het eerste huisje dat we tegenkomen
    target_huis = Huisje.query.first()

    # 3. Zoek een gebruiker die de boeking maakt (we pakken de eerste user)
    # Zorg dat je wel een user in je DB hebt!
    target_user = User.query.first()

    if not target_huis or not target_user:
        print("Fout: Geen huisje of gebruiker gevonden in de database. Seed eerst de huisjes en users!")
    else:
        print(f"Boekingen toevoegen aan: {target_huis.beschrijving} voor gast: {target_user.username}")

        # 4. Maak 10 boekingen aan voor verschillende weken
        for week in range(1, 11):  # Week 1 tot en met 10
            nieuwe_boeking = Boeking(
                gast_id=target_user.id,
                huis_id=target_huis.id,
                weeknummer=week
            )
            db.session.add(nieuwe_boeking)

        # 5. Opslaan
        db.session.commit()
        print(f"Succes! 10 boekingen toegevoegd aan huisje ID: {target_huis.id}")
