# Personalized Marketing and Customer Experience
# All-in-one Python program

# Sample customer data
customers = [
    {"name": "Alice", "interests": ["electronics", "books"]},
    {"name": "Bob", "interests": ["fashion", "sports"]},
    {"name": "Charlie", "interests": ["books", "home"]}
]

# Sample product catalog
products = {
    "electronics": ["Smartphone", "Laptop", "Headphones"],
    "books": ["Python Programming", "Data Science 101", "AI for Beginners"],
    "fashion": ["T-Shirts", "Sneakers", "Jeans"],
    "sports": ["Football", "Tennis Racket", "Yoga Mat"],
    "home": ["Cushions", "Lamps", "Kitchen Set"]
}

# Function to recommend products
def recommend_products(customer):
    name = customer["name"]
    interests = customer["interests"]
    recommended = []

    for interest in interests:
        recommended.extend(products.get(interest, []))

    return name, recommended

# Main logic
def main():
    print("=== Personalized Recommendations ===\n")
    for customer in customers:
        name, recommendations = recommend_products(customer)
        print(f"Hi {name}, based on your interests, we recommend:")
        for item in recommendations:
            print(f" - {item}")
        print("\n")

if __name__ == "__main__":
    main()
