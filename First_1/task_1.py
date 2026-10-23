raw = [
    {"name": " laptop ", "price": "55000", "category": "electronics"},
    {"name": "Mouse", "price": 500, "category": "Electronics"},
    {"name": "mouse", "price": "500", "category": "Electronics"},  
    {"name": "Desk", "price": "7500.50", "category": "furniture"},
    {"name": "Chair", "price": None, "category": "Furniture"},      
    {"name": "Pen", "price": "abc", "category": "Stationery"},      
]

clean = []          
seen = set()     

for item in raw:
    name = item["name"].strip().title()
    category = item["category"].strip().title()
    price = item["price"]

    if price is None:                           
        continue
    try:
        price = float(price)                     
    except ValueError:                         
        continue
    if name in seen:                             
        continue

    seen.add(name)
    clean.append({"name": name, "price": price, "category": category})
groups = {}
for p in clean:
    if p["category"] not in groups:
        groups[p["category"]] = []
    groups[p["category"]].append(p)
for category in groups:
    print(category.upper())
    for p in groups[category]:
        print("  ", p["name"], "-", p["price"])
print("Total products:", len(clean))

