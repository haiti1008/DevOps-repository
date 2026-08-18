import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_all_users():
    url = f"{BASE_URL}/users"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return []

def get_user_posts(user_id):
    url = f"{BASE_URL}/posts"
    params = {"userId": user_id}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return []

def display_users(users):
    print("\n=== ALL USERS ===")
    print(f"{'ID':<5} {'Name':<25} {'Email':<35} {'City':<15}")
    print("-" * 80)
    for user in users:
        print(f"{user['id']:<5} {user['name']:<25} {user['email']:<35} {user['address']['city']:<15}")

def display_posts(posts, user_name):
    print(f"\n=== POSTS BY {user_name.upper()} ===")
    print(f"Total posts: {len(posts)}\n")
    for i, post in enumerate(posts[:3], 1):
        print(f"Post {i}: {post['title']}")
        print(f"  Body: {post['body'][:80]}...")
        print()

def main():
    print("=== JSONPlaceholder API Experiment ===\n")
    users = get_all_users()
    display_users(users)
    if users:
        first_user = users[0]
        posts = get_user_posts(first_user['id'])
        display_posts(posts, first_user['name'])
    print("=== Experiment Complete ===")

if __name__ == "__main__":
    main()

