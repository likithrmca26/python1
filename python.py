text = input("Enter the amount: ")

if text.isdigit():
    amount = int(text)

    notes = {
        100: 0,
        50: 0,
        10: 0
    }

    for note in notes:
        notes[note], amount = divmod(amount, note)

    for note, count in notes.items():
        print(f"{note} rupee note(s): {count}")
else:
    print("Invalid amount!")
