# Exercise 5

talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots =  float(input("Enter lots: "))
gTotal = (
    talents * 20 * 32 * 13.3 +
    pounds * 32 * 13.3 +
    lots * 13.3
)
kgWeight = int(gTotal // 1000)
grams = gTotal % 1000

print(f"The weight in modern units: \n{kgWeight} kilograms and {grams: .2f} grams")
