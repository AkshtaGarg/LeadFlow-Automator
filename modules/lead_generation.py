import pandas as pd
import os

def generate_leads(industry="General", count=10):
    # Ensure directory exists
    os.makedirs("data/raw", exist_ok=True)

    leads = []

    for i in range(1, count + 1):
        leads.append({
            "name": f"{industry} Business {i}",
            "city": "Delhi",
            "industry": industry,
            "contact_person": "N/A",
            "email": f"business{i}@example.com"
        })

    df = pd.DataFrame(leads)
    df.to_csv("data/raw/leads.csv", index=False)

    print(f"✅ {count} leads generated for {industry}")

if __name__ == "__main__":
    generate_leads("Real Estate", 10)