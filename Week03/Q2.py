cart =["apple", "banana", "milk", "bread","apple", "eggs"]
apple_count = cart.count("apple")
print(f"Number of apples in the cart: {apple_count}")
print(f"The index of 'milk' in the cart: {cart.index('milk')}")
cart.remove("banana")
print(f"Cart after removing 'banana': {cart}")  
print(f"removing an item with pop(): {cart.pop()}")
print("Is banana still in the cart?", "banana" in cart)
print(f"Final cart contents: {cart}")