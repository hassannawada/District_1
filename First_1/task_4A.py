raw = [
    {"name": "laptop", "price": "55000", "category": "electronics"},
    {"name": "Phone", "price": 30000, "category": "Electronics"},
    {"name": "phone", "price": 30000, "category": "electronics"},   
    {"name": "Tablet", "price": None, "category": "Electronics"},   
    {"name": "Camera", "price": "42000", "category": "electronics"},
    {"name": "Mouse", "price": 500, "category": "Electronics"},
    {"name": "Desk", "price": 7500, "category": "furniture"},
    {"name": "Chair", "price": "4500", "category": "Furniture"},
]


valid = [p for p in raw if p["price"] is not None]

unique = {
    p["name"].strip().title(): {"name": p["name"].strip().title(),
                                "price": float(p["price"]),
                                "category": p["category"].strip().title()}
    for p in valid
}
products = list(unique.values())
categories = {p["category"] for p in products}
groups = {c: [p for p in products if p["category"] == c] for c in categories}

top5 = {c: sorted(items, key=lambda p: p["price"], reverse=True)[:5]
        for c, items in groups.items()}

summary = {c: [(p["name"], p["price"]) for p in items] for c, items in top5.items()}

print(summary)

print([p["name"] for items in top5.values() for p in items])
