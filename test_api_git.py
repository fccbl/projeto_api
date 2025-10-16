import requests 
import pytest

# --- REQUISIÇÃO SIMPLES ---
def test_simple_request():
    response = requests.get("https://api.github.com")
    assert response.status_code == 200

# --- REQUISIÇÃO USER ---
def test_get_specific_user():
    response = requests.get("https://api.github.com/users/fccbl")
    data = response.json()
    assert data["login"] == "fccbl"
    print(f"Usuário: {data['login']}")
#pytest - s (para aparecer na tela)

# --- Validate User Type---
def test_validate_user():
    response = requests.get("https://api.github.com/users/fccbl")
    data = response.json()
    assert data["type"] == "User"

# --- Request with Repository ID---
def test_request_repo_id():
    response = requests.get("https://api.github.com/user/232577379")
    data = response.json()
    assert data["id"] == 232577379 and data["login"] == "fccbl"
    
# --- Handling Errors (Non-existent User)--
def test_handliing_error():
    response = requests.get("https://api.github.com/users/nonexistentuser12345")
    data = response.json()
    assert data["message"] == "Not Found"

# ---  List User Repositories--

def test_list_user_repo():
    response = requests.get("https://api.github.com/users/google/repos?per_page=5")
    data = response.json()
    print(f"Nome: {data[0]['name']}")

# --- Navigate Follower Pagination --

def test_step_7():
    microsoft_followers = requests.head("https://api.github.com/users/microsoft/followers")
    microsoft_next_page_link = microsoft_followers.links["next"]["url"]
    print(microsoft_next_page_link)
    micro_follows = requests.get(microsoft_next_page_link)
    assert micro_follows.status_code == 200

# --- Count a User's Public Repositories --

def test_count_users_public_repo():
    response = requests.get("https://api.github.com/users/facebook")
    data = response.json()
    print(f"O facebook tem {data['public_repos']}repositorios")

# ---  Find a Specific Language in a Repository--

def test_specific_language():
    response = requests.get("https://api.github.com/repos/facebook/react/languages")
    data = response.json()
    print(f"JavaScript:{data['JavaScript']}")

# ---  Explore Another Endpoint (Emojis) --

def test_emojis():
    response = requests.get("https://api.github.com/emojis")
    dados = response.json()
    
    if "+1" in dados:
        print("+1 existe no emoji")
    else:
        print("+1 nao existe")
    
    