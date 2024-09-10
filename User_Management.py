import requests
import json

# Define the base URL and headers (Bearer Token Authorization)
BASE_URL = "https://gorest.co.in/public/v2/users"
TOKEN = "6e0737ba963e249ce897fd8b590a3facf38fd290b2a25e44deb1ef0e3fd75e42"
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# Function to create a user (POST)
def create_user():
    url = BASE_URL
    payload = {
        "name": "John Doe",
        "gender": "male",
        "email": "john.doe123@example.com",
        "status": "active"
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        user_data = response.json()
        print(f"User Created: {json.dumps(user_data, indent=4)}")
        return user_data["id"]  # Return the created user ID
    else:
        print(f"Failed to create user: {response.status_code}")
        print(response.text)
        return None

# Function to retrieve a user by ID (GET)
def retrieve_user(user_id):
    url = f"{BASE_URL}/{user_id}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        print(f"User Retrieved: {json.dumps(user_data, indent=4)}")
    else:
        print(f"Failed to retrieve user: {response.status_code}")
        print(response.text)

# Function to update a user's info (PUT)
def update_user(user_id):
    url = f"{BASE_URL}/{user_id}"
    payload = {
        "name": "John Jay Doe",
        "email": "John.Jay.Doe123@example.com"
    }
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 200:
        updated_user_data = response.json()
        print(f"User Info Updated: {json.dumps(updated_user_data, indent=4)}")
    else:
        print(f"Failed to update user: {response.status_code}")
        print(response.text)

# Function to update a user's status (PATCH)
def update_status(user_id):
    url = f"{BASE_URL}/{user_id}"
    payload = {
        "status": "inactive"
    }
    response = requests.patch(url, headers=headers, json=payload)
    if response.status_code == 200:
        updated_status_data = response.json()
        print(f"User Status Updated: {json.dumps(updated_status_data, indent=4)}")
    else:
        print(f"Failed to update user status: {response.status_code}")
        print(response.text)

# Function to delete a user (DELETE)
def delete_user(user_id):
    url = f"{BASE_URL}/{user_id}"
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"User {user_id} deleted successfully.")
    else:
        print(f"Failed to delete user: {response.status_code}")
        print(response.text)


# Main function to run the test flow
def main():
    # 1. Create a new user (POST)
    user_id = create_user()

    if user_id:
        # 2. Retrieve the user information (GET)
        retrieve_user(user_id)

        # 3. Update the user's information (PUT)
        update_user(user_id)

        # 4. Partially update the user's status (PATCH)
        update_status(user_id)

        # 5. Delete the user (DELETE)
        delete_user(user_id)

if __name__ == "__main__":
    main()