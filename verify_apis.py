import requests
import json

BASE_URL = "http://127.0.0.1:8000/api"
EMAIL = "admin@example.com"
PASSWORD = "password"

def run_verification():
    print(f"Verifying APIs at {BASE_URL}...")

    # 1. Login
    login_url = f"{BASE_URL}/accounts/token/"
    # Note: Login endpoint expects 'username' but we send email in username field as per custom backend
    resp = requests.post(login_url, json={"username": EMAIL, "password": PASSWORD})
    if resp.status_code != 200:
        print(f"Login failed: {resp.text}")
        return
    
    tokens = resp.json()
    access_token = tokens['access']
    headers = {"Authorization": f"Bearer {access_token}"}
    print(f"Login successful. Token obtained.")

    # 2. Stats
    resp = requests.get(f"{BASE_URL}/accounts/admin/stats/", headers=headers)
    if resp.status_code == 200:
        print(f"Stats API: OK - {resp.json()}")
    else:
        print(f"Stats API failed: {resp.text}")

    # 3. Users
    resp = requests.get(f"{BASE_URL}/accounts/admin/users/", headers=headers)
    if resp.status_code == 200:
        print(f"Users API: OK - Found {len(resp.json())} users")
    else:
        print(f"Users API failed: {resp.text}")

    # 4. Products (CRUD)
    # List
    resp = requests.get(f"{BASE_URL}/products/")
    print(f"Products List: OK - Found {len(resp.json())} products")

    # Create
    new_product = {
        "id": "verify-test-product",
        "name": "Verify Test Product",
        "price": "99.99",
        "display_price": "$99.99",
        "color": "Test Color",
        "image": "http://example.com/image.jpg",
        "description": "Test verification product",
        "slug": "verify-test-product",
        "features": [],
        "sizes": []
    }
    resp = requests.post(f"{BASE_URL}/products/", json=new_product, headers=headers)
    if resp.status_code == 201:
        print("Product Create: OK")
    else:
        print(f"Product Create failed: {resp.text}")

    # Delete
    resp = requests.delete(f"{BASE_URL}/products/verify-test-product/", headers=headers)
    if resp.status_code == 204:
        print("Product Delete: OK")
    else:
        print(f"Product Delete failed: {resp.text}")

    # 5. Orders
    resp = requests.get(f"{BASE_URL}/orders/", headers=headers)
    if resp.status_code == 200:
        print(f"Orders API: OK - Found {len(resp.json())} orders")
    else:
        print(f"Orders API failed: {resp.text}")

    # 6. Tickets
    resp = requests.get(f"{BASE_URL}/tickets/", headers=headers)
    if resp.status_code == 200:
        print(f"Tickets API: OK - Found {len(resp.json())} tickets")
    else:
        print(f"Tickets API failed: {resp.text}")

if __name__ == "__main__":
    run_verification()
