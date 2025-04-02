import vinglePetter
import vinglePetterAvansert
import vinglePetterBasic


def hovedmeny():
    while True:
        print("Hovedmeny")
        print('1. Gå til vinglepetter basic')
        print('2. Gå til vinglepetter alpha')
        print('3. Gå til vinglepetter avansert')
        print('4. Avslutte programmet')

        choice = input("Velg ett alternativ: ")
        if choice == '1':
            print('Du valgte vinglepetter veldig basic')
            vinglePetter.start_veldig_basic()
        elif choice == '2':
            print("Du valgte vinglepetter alpha")
            vinglePetterBasic.start_basic()
        elif choice == '3':
            print("Du valgte vinglepetter avansert")
            vinglePetterAvansert.start_avansert()
        elif choice == '4':
            print("Du avslutter programmet")
            break
        else:
            print("Ugyldig valg")

hovedmeny()