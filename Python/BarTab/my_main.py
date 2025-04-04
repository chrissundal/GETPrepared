from bar_tab import Tab
tables = {
    'Bord 1': Tab(),
    'Bord 2': Tab(),
    'Bord 3': Tab(),
    'Bord 4': Tab(),
    'Bord 5': Tab(),
    'Bord 6': Tab(),
    'Bord 7': Tab(),
    'Bord 8': Tab(),
    'Bord 9': Tab(),
    'Bord 10': Tab()
}
bord_navn = list(tables.keys())
while True:
    for i, navn in enumerate(bord_navn):
        print(f'{i+1}{'.':1} {navn}') if i == 9 else print(f'{i+1}{'.':2} {navn}')

    selected_index = int(input('Hvilket bord vil du ta? (1-10): '))
    selected_name = bord_navn[selected_index -1]
    my_table = tables[selected_name]
    print(f'Du har valgt {selected_name}')
    print()
    while True:
        num = 0
        for item in Tab.menu:
            print(f'{num}. {item}: {Tab.menu[item]} kr')
            num += 1

        keys_list = list(Tab.menu.keys())
        choice = input('Hva vil du ha? (ferdig? skriv "f"): ')
        if choice == 'f': break
        selected_item = keys_list[int(choice)]
        print(selected_item)
        my_table.add_item(selected_item)

    try:
        tips = int(input('Hvor mye vil du gi i tips? (%): '))
    except ValueError:
        print("Ugyldig tipsbeløp, standard 10% tips er valgt.")
        tips = 10

    print()
    my_table.print_bill(15,tips)
    if input('Vil du ta en ny bestilling? (j/n): ') == 'n': break
print("\n===== DAGENS TOTALE SALG =====")
day_total = 0
for name, table in tables.items():
    table_total = table.print_total_day()
    if table_total > 0:
        print(f"{name}: {table_total:.2f} kr")
        day_total += table_total

print(f"\nTotalt salg for dagen: {day_total:.2f} kr")
