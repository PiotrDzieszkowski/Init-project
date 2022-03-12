shopping_list = {"Piekarnia": ["Chleb", "Pączek", "Bułki"],
"Warzywniak": ["Marchew", "Seler", "Rukola"]}
for sklep,produkty in shopping_list.items():
    print("Idę do", sklep, "i kupuje tam", produkty)
for products in shopping_list.values():
    print("W sumie kupuję", len(products), "produktów")