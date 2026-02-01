
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",  
    "Charlie": "555-8765",
}

print(f"Alice's contact number: {contacts['Alice']}")
contacts["David"] = "555-4321"
print(f"Updated contacts: {contacts}")
contacts["Bob"] = "555-0000"
print(f"Contacts after updating Bob's number: {contacts}")
del contacts["Charlie"]
print(f"Contacts after removing Charlie: {contacts}")
print(f"Total contacts: {len(contacts) }")
print(f"All names: {contacts.keys( )}")
print(f"All numbers: {contacts.values( )}")

