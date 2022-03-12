shopping_list = {"piekarnia": ["chleb", "pączek", "bułki"],
"warzywniak": ["marchew", "seler", "rukola"]}
for sklep,produkty in shopping_list.items():
    print("Idę do", sklep.capitalize(), "i kupuje tam", produkty)

total = 0
for value in shopping_list:
    value_list = shopping_list[value]
    count = len(value_list)
    total += count
print("W sumie kupuję", {total}, "produktów")

print("Hiszpanska inkwizycja")
