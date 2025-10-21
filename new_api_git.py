import pytest

#01
def test_simple_request(api_client, github_base_url):
    response = api_client.get(github_base_url)
    assert response.status_code == 200

#02
def test_get_specific_user(api_client, github_base_url):
    response = api_client.get(f"{github_base_url}/users/fccbl")
    data = response.json()
    assert data["login"] == "fccbl"

#03
def test_validate_user(api_client, github_base_url):
    response = api_client.get(f"{github_base_url}/users/fccbl")
    data = response.json()
    assert data["type"] == "User"

#04
def test_request_repo_id(api_client, github_base_url):
    response = api_client.get(f"{github_base_url}/user/232577379")
    data = response.json()
    assert data["id"] == 232577379 and data["login"] == "fccbl"

#05
def test_handling_error(api_client, github_base_url):
    response = api_client.get(f"{github_base_url}/users/nonexistentuser12345")
    data = response.json()
    assert data["message"] == "Not Found"

#06
def test_list_user_repo(api_client, github_base_url):
    response = api_client.get(f"{github_base_url}/users/google/repos?per_page=5")
    data = response.json()
    assert response.status_code == 200
    print(f"Primeiro repositório: {data[0]['name']}")

#07
def test_followers_pagination(api_client, github_base_url):
    head_response = api_client.head(f"{github_base_url}/users/microsoft/followers")
    next_link = head_response.links.get("next", {}).get("url")
    if next_link:
        next_page = api_client.get(next_link)
        assert next_page.status_code == 200

#08
def test_count_users_public_repo(api_client, github_base_url):
    response = api_client.get(f"{github_base_url}/users/facebook")
    data = response.json()
    print(f"O Facebook tem {data['public_repos']} repositórios públicos")

#09
def test_specific_language(api_client, github_base_url):
    response = api_client.get(f"{github_base_url}/repos/facebook/react/languages")
    data = response.json()
    assert "JavaScript" in data
    print(f"JavaScript: {data['JavaScript']}")

#10
def test_emojis(api_client, github_base_url):
    response = api_client.get(f"{github_base_url}/emojis")
    data = response.json()
    assert "+1" in data
