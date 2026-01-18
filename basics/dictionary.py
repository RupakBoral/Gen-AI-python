

users = [
    {"id": "1", "total": 100, "coupon": "C10"},
    {"id": "2", "total": 200, "coupon": "C20"},
    {"id": "3", "total": 300, "coupon": "C30"},
    {"id": "3", "total": 300}
]


discounts = {
    "C10": (0.1, 0.1),
    "C20": (0.2, 0.2),
    "C30": (0.3, 0.3)
}


for user in users:
    percentage, hidden_amount = discounts.get(user.get("coupon", 0), (0, 0))
    amount = user.get("total")*(1 - percentage) + hidden_amount
    print(f"User {user.get("id", "No id")} paid {amount}")
    
    