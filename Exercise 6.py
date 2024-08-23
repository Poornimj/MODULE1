# Exercise 6
import random
print(f"First combination of Lock number {random.randint(0,999):03d}")
four_code = str(random.randint(1, 6)) + str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1, 6))
print("Second combination of lock number " + four_code)