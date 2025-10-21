import pytest
from conftest import load_csv_test_cases
#01

test_post = load_csv_test_cases("test_cases.csv")
@pytest.mark.parametrize("test_case", test_post)

def test_post_create(api_client, base_url, test_case):
    url = f"{base_url}/posts"
    data = {
        "userId": int(test_case["userId"]),
        "title": test_case["title"],
        "body": test_case["body"]
    }
    response = api_client.post(url, json=data)
    assert response.status_code == 201
    json_data = response.json()
    assert json_data["userId"] == int(test_case["userId"])
    assert json_data["title"] == test_case["title"]
    assert json_data["body"] == test_case["body"]
#02
def test_validate_created(api_client, base_url):
    url = f"{base_url}/posts"
    data = {"userId": 1, "title": "Meu post", "body": "Conteúdo"}
    response = api_client.post(url, json=data)
    json_data = response.json()
    assert response.status_code == 201
    assert json_data["title"] == "Meu post"
    assert json_data["body"] == "Conteúdo"

#03
def test_update_post(api_client, base_url):
    url = f"{base_url}/posts/1"
    data = {"userId": 1, "title": "Meu novo post", "body": "Conteúdo atualizado"}
    response = api_client.put(url, json=data)
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["title"] == "Meu novo post"
    assert json_data["body"] == "Conteúdo atualizado"

#04
def test_delete_post(api_client, base_url):
    url = f"{base_url}/posts/1"
    response = api_client.delete(url)
    assert response.status_code == 200

#05
def test_list_all_users(api_client, base_url):
    url = f"{base_url}/users"
    response = api_client.get(url)
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 10

#06
def test_specific_user(api_client, base_url):
    url = f"{base_url}/users/5"
    response = api_client.get(url)
    data = response.json()
    assert data["name"] == "Chelsey Dietrich"

#07
def test_new_comment(api_client, base_url):
    url = f"{base_url}/posts/1/comments"
    data = {"userId": 1, "name": "Fabiana", "body": "Comentário"}
    response = api_client.post(url, json=data)
    json_data = response.json()
    assert response.status_code == 201
    assert json_data["name"] == "Fabiana"

#08
def test_users_album(api_client, base_url):
    url = f"{base_url}/users/3/albums"
    response = api_client.get(url)
    data = response.json()
    assert response.status_code == 200
    assert len(data) > 0

#09
def test_photos_album(api_client, base_url):
    url = f"{base_url}/albums/2/photos"
    response = api_client.get(url)
    data = response.json()
    assert response.status_code == 200
    expected_title = "reprehenderit est deserunt velit ipsam"
    for photo in data:
        assert expected_title not in photo["title"]

#10
def test_new_task(api_client, base_url):
    url = f"{base_url}/todos"
    data = {"userId": 1, "title": "Learn Pytest", "body": "Conteúdo novo"}
    response = api_client.post(url, json=data)
    json_data = response.json()
    assert response.status_code == 201
    assert json_data["title"] == "Learn Pytest"

#11
def test_update_task(api_client, base_url):
    url = f"{base_url}/todos/5"
    data = {"completed": True}
    response = api_client.patch(url, json=data)
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["completed"] is True

#12
def test_users_completed_tasks(api_client, base_url):
    url = f"{base_url}/todos?userId=1&completed=true"
    response = api_client.get(url)
    data = response.json()
    assert response.status_code == 200
    assert all(task["completed"] for task in data)

#13
def test_validate_comment_structure(api_client, base_url):
    url = f"{base_url}/comments/10"
    response = api_client.get(url)
    data = response.json()
    expected_keys = ["postId", "id", "name", "email", "body"]
    for key in expected_keys:
        assert key in data

#14
def test_delete_comment(api_client, base_url):
    url = f"{base_url}/comments/3"
    response = api_client.delete(url)
    assert response.status_code == 200

#15
def test_create_invalid_data(api_client, base_url):
    url = f"{base_url}/posts"
    data = {}
    response = api_client.post(url, json=data)
    assert response.status_code == 201

#16
def test_users_post(api_client, base_url):
    url = f"{base_url}/users/7/posts"
    response = api_client.get(url)
    data = response.json()
    assert response.status_code == 200
    print(f"O user 7 tem {len(data)} posts")

#17
def test_update_email(api_client, base_url):
    url = f"{base_url}/users/2"
    data = {"email": "new.email@example.com"}
    response = api_client.put(url, json=data)
    assert response.status_code == 200

#18
def test_final_challenge(api_client, base_url):
    url = f"{base_url}/posts"
    data = {"userId": 1, "title": "Meu post", "body": "Conteúdo", "comments": "desafio"}
    response = api_client.post(url, json=data)
    json_data = response.json()
    assert response.status_code == 201
    assert json_data["userId"] == 1
