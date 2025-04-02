def start_avansert():
    while True:
        try:
            print("Svar på følgende spørsmål med en score fra 0 til 5:\n")
            time = int(input("Hvor mye tid vil oppgaven ta? (1 = lite, 5 = veldig mye): "))
            difficulty = int(input("Hvor komplisert er oppgaven? (1 = enkelt, 5 = veldig komplisert): "))
            interest = int(input("Hvor interessert er du i å gjøre dette? (1 = ikke interessert, 5 = veldig interessert): "))
            value = int(input("Hvor nyttig tror du dette vil være? (1 = ikke nyttig, 5 = veldig nyttig): "))
            risk = int(input("Hvor stor risiko er involvert? (1 = lav, 5 = høy): "))
            score = (interest + value) - (time + difficulty + risk)

            print("\nResultatene dine er klare...")
            if score >= 5:
                print(f"Totalt score: {score} - Du burde definitivt gjøre det!")
            elif score >= 2:
                print(f"Totalt score: {score} - Det kan være verdt å gjøre det.")
            elif score > 0:
                print(f"Totalt score: {score} - Det kan vurderes, men i utgangspunktet en dårlig ide.")
            else:
                print(f"Totalt score: {score} - Du burde ikke gjøre det.")
            print()
            final = input('Igjen? (1 = ja, 2 = nei)')
            print()
            if final == '2': break
        except ValueError:
            print('skriv ett gyldig tall')
