import requests

def get_user_by_id(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        print("Request failed")

def create_user(name,email):
    url = "https://jsonplaceholder.typicode.com/users"
    create = {
        "name":name,
        "email":email
    }
    response = requests.post(url,json=create)
    response.raise_for_status()
    return response.json()

def update_user(user_id,name,email):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    update = {
        "name":name,
        "email":email
    }
    response = requests.put(url,json=update)
    response.raise_for_status()
    return response.json()

def delete_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    try:
        response = requests.delete(url)
        return response.raise_for_status()
        #return response.json()
    except requests.exceptions.RequestException:
        print("No such user")

def patch_user(user_id, email):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    updated_data = {
        "email": email
    }

    try:
        response = requests.patch(url, json=updated_data)
        response.raise_for_status()
        print("Status:", response.status_code)
        return response.json()

    except requests.exceptions.RequestException:
        print("Unable to update user")

while True:
    print("1. Get user")
    print("2. Create user")
    print("3. Update user")
    print("4. Delete user")
    print("5. Patch user")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        user_id = input("Enter your id: ")
        print(get_user_by_id(user_id))
    elif choice == 2:
        create_user(input("Enter your name: "), input("Enter your email: "))
    elif choice == 3:
        update_user(input("Enter your id: "), input("Enter your name: "), input("Enter your email: "))
    elif choice == 4:
        delete_user(input("Enter your id: "))
    elif choice == 5:
        patch_user(input("Enter your id: "),input("Enter your email: "))
    elif choice == 6:
        print("Exit")
        break
    else:
        print("Invalid choice")

