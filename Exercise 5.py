import math
# Exercise 5
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots =  float(input("Enter lots: "))
kg_weight = ((talents*20+pounds)*32 + lots)*8.0133
gr_weight = 1000.0*(kg_weight - int(kg_weight))
print(f"The weight in modern units: \n {int(kg_weight)} kilograms and {gr_weight: .2f} grams")
