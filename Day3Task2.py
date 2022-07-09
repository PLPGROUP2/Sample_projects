#Prompt the use to enter the number of fat grams they consumed
fat_grams=float(input("Enter number of fat grams consumed: "))
#Prompt the use to enter the number of carbohydrate grams they consumed
carbs_grams=float(input("Enter number of carbs grams consumed: "))

#create a variables to hold value for fat and carbs calories using the formulae
fat_calories=fat_grams*9

carbs_calories=carbs_grams*4

#printing results for fat calories and carb calories
print("Calories from fats:", fat_calories)
print("Calories from carbohydrates:", carbs_calories)
