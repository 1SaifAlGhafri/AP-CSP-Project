prayer_beads = ["Amber", "Quartz", "Kuk", "Bakelite", "Labradorite"]
prices = [10, 7, 8, 5, 6]
weights = [20, 25, 22, 18, 24]
strings = ["Silk", "Nylon", "Cotton", "Supreme Silk", "Supreme Nylon"]
quality = ["Premium", "Standard", "High", "Collector", "Limited"]
tassels = ["Gold", "Silver", "Brown", "Black", "Blue"]

def calculate_cost(name, quantity):
    name = name.capitalize()
    for i in range(len(prayer_beads)):
        if name == prayer_beads[i]:
            return prices[i] * weights[i] * quantity
    return 0

def show_details(name):
    name = name.capitalize()
    for i in range(len(prayer_beads)):
        if name == prayer_beads[i]:
            print("Prayer Beads Details")
            print("Price/g:", prices[i])
            print("Weight:", weights[i])
            print("String:", strings[i])
            print("Quality:", quality[i])
            print("Tassel:", tassels[i])
            return
    print("Prayer beads not found.")


print("We have:", ", ".join(prayer_beads))

name_choice = input("Enter the Prayer Beads you want to buy: ")
quantity = int(input("Enter number of Prayer Beads: "))

show_details(name_choice)

total = calculate_cost(name_choice, quantity)
print("The total cost is:", total, "AED")
