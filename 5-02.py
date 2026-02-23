def make_change(target_amount):
    
    denominations = [200, 100, 50, 20, 10, 5, 2, 1]
    amount = 0
    notes = []
    for amount_type in denominations:
        while target_amount >= amount_type:
            target_amount -= amount_type
            notes.append(amount_type)
            amount += 1
    return amount, notes


value = input("Enter the amount to change: ")
amount, notes = make_change(int(value))

print(f"The min amount of notes for {value} is {amount} which are {notes}") 