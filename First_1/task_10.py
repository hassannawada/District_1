import asyncio
import os
from pathlib import Path
from dotenv import load_dotenv

# Looks for the .env file in the exact same directory as this script
load_dotenv(Path(__file__).resolve().parent / ".env")

async def get_sales(key):
    await asyncio.sleep(2)
    return {"source": "Sales", "records": 120}

async def get_users(key):
    await asyncio.sleep(1)
    return {"source": "Users", "records": 80}

async def get_stock(key):
    await asyncio.sleep(3)
    return {"source": "Stock", "records": 45}

async def main():
    sales_key = os.getenv("SALES_KEY")
    users_key = os.getenv("USERS_KEY")
    stock_key = os.getenv("STOCK_KEY")
    
    # Validation check for the keys
    if not (sales_key and users_key and stock_key):
        print("Keys not found. Check your .env file")
        return

    print("Fetching data asynchronously... Please wait.")
    results = await asyncio.gather(
        get_sales(sales_key),
        get_users(users_key),
        get_stock(stock_key),
    )
    
    print("\n=== DASHBOARD ===")
    total = 0
    for r in results:
        print(f"{r['source']} -> {r['records']} records")
        total += r['records']
    print("Total records:", total)

if __name__ == "__main__":
    asyncio.run(main())
