summe_warenkorb = 0

while True:
    if summe_warenkorb != 0:
        print(" ### Tarifauskunftsrechner Museum XXX ### ")
    else:
        print("Wählen Sie weiteres Ticket! Aktueller Warenkorb: " , summe_warenkorb )

    print(" Hallo, geben Sie bitte Ihr Alter ein.")
    alter_gast = int(input())

    print("Wollen Sie einen ganzene oder halben Tag bleiben! (g (ganztag) / h (halbtags))")
    tag_eingabe = input()

    if tag_eingabe == 'g':
        preis_erwachsene = 10.0
        preis_kinder = 5.0
        preis_jugend = 6.0
        preis_premium = 6.0
        preis_basis = 8.0
    else:
        preis_erwachsene = 5.0
        preis_kinder = 2.5
        preis_jugend = 3.5
        preis_premium = 3.0
        preis_basis = 4.0
        
    if alter_gast < 14:
        print(" ### Eintritt Kinder ### ")
        summe_warenkorb += preis_kinder
        print(" Preis: ", preis_kinder, " Euro ")
    elif alter_gast < 18:
        print(" ### Eintritt Jugendliche ### ")
        summe_warenkorb += preis_jugend
        print(" Preis: ", preis_jugend, " Euro ")  
    else:
        print(" Sind Sie Mitglied im Duisburger Museumsclub? (Nachweis erforderlich) ")
        print(" Wenn Sie Premium-Mitglied sind, geben Sie 'p' ein.")
        print(" Wenn Sie Basis-Mitglied sind, geben Sie 'b' ein.")
        print(" Wenn Sie kein Mitglied sind, drücken Sie eine beliebige andere Taste. ")
        antwort_rabatt = input();
        if antwort_rabatt == "p":
            sekt = input("Wollen Sie ein zusätzliches Sekt haben? (j (Ja) / n (Nein)): ")
            print(" ### Eintritt Premium-Mitglied ### ")
            if sekt.lower() == 'j':
                summe_warenkorb += preis_premium + 0.75
                print(" Preis: ", preis_premium + 0.75 , " Euro ")
            else:
                summe_warenkorb += preis_premium
                print(" Preis: ", preis_premium, " Euro ")
                
        elif antwort_rabatt == "b":
            print(" ### Eintritt Basis-Mitglied ### ")
            summe_warenkorb += preis_basis
            print(" Preis: ", preis_basis, " Euro ")
        else:
            print(" ### Eintritt Erwachsene (voller Preis) ### ")
            summe_warenkorb += preis_erwachsene
            print(" Preis: ", preis_erwachsene, " Euro")
            
    print("Viel Spaß!")

    nochmal = input("Wollen Sie einen Weiteren Tarif abfragen? (j (Ja) / n (Nein)): ")
    if nochmal.lower() != 'j':
        break