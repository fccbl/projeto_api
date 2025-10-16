import requests 
import pytest

#Create a New Post (POST)
def test_post_create():

    url = "https://jsonplaceholder.typicode.com/posts"
    data = {"userId": 1, "title": "Meu post", "body": "Conteúdo"}
    create_post = requests.post(url, json = data)
    assert create_post.status_code == 201
    create = create_post.json()
    print(create)

#Validate Created Post Data
def test_validate_created():

    url = "https://jsonplaceholder.typicode.com/posts"
    data = {"userId": 1, "title": "Meu post", "body": "Conteúdo"}
    create_post = requests.post(url, json = data)
    assert create_post.status_code == 201
    create = create_post.json()

    assert create["title"] == "Meu post", f"Título incorreto: {create['title']}"
    assert create["body"] == "Conteúdo", f"Body incorreto: {create['body']}"

#Update a Post (PUT)

def test_update():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    data_update = {"userId":1, "title": "Meu novo post", "body": "Conteúdo novo"}

    update_put = requests.put(url, json= data_update)

    update_request = update_put.json()

    print(update_request)

    assert update_put.status_code == 200 

#Validate Post Update

def test_validade_update():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    data_update = {"userId":1, "title": "Meu novo post", "body": "Conteúdo novo"}

    update_put = requests.put(url, json= data_update)

    update_request = update_put.json()

    assert update_request["title"] ==  "Meu novo post"
    assert update_request["body"] == "Conteúdo novo"
 

    assert update_put.status_code == 200 

#Delete a Post (DELETE)

def test_delete():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.delete(url)

    assert response.status_code == 200

    print("O post com o ID 1 foi deletado")

#List All Users

def test_list_all_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()
    assert len(data) == 10
    print("Possui 10 listas de usuarios")

# Fetch a Specific User

def specific_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/5")
    data = response.json()
    assert data["name"] == "Chelsey Dietrich"

# Create a New Comment for a Post

def test_new_comment():
    url = "https://jsonplaceholder.typicode.com/posts/1/comments"
    data = {"userId": 1, "name": "Fabiana", "body": "Comentário"}
    add_post = requests.post(url, json= data)
    post_json =add_post.json()
    assert add_post.status_code == 201
    print(post_json)

#List a User's Albums
def test_users_album():
    response = requests.get("https://jsonplaceholder.typicode.com/users/3/albums")
    data = response.json()
    print(f"O usuário possui {len(data)} álbuns")

#List Photos in an Album

def test_photos_album():
    response = requests.get("https://jsonplaceholder.typicode.com/albums/2/photos")
    data = response.json()
    expective_title = "reprehenderit est deserunt velit ipsam"

    assert data[0]["title"] == expective_title, f"Título esperado: '{expective_title}', mas foi: '{data[0]['title']}'"