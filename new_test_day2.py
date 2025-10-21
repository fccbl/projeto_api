from conftest import load_csv_test_cases

def test_id2(base_url, api_client):
    
    response = api_client.get(f"{base_url}/comments?postId=2")
    assert response.status_code == 200
    response_json = response.json()

    for comment in response_json:
        assert comment["postId"] == 2

    print(f"Foram encontrados {len(response_json)} comentários para o post 2.")

#2
def test_all_user(base_url, api_client):
    response = api_client.get(f"{base_url}/todos?userId=5")

    assert response.status_code == 200 

    response_json = response.json()

    assert response_json is not None

#3
def test_album(base_url, api_client):
      response = api_client.get(f"{base_url}/albums?userId=9")
      response_json = response.json()
      assert len(response_json) == 10
      print(f"O usuario possui {len(response_json)} albumns")

#4
def test_list_all(base_url, api_client):
       response = api_client.get(f"{base_url}/todos?userId=1&completed=true")
       response_json = response
       assert response.status_code == 200

#5
def test_headers(httpbin_url, api_client):
      
      data = {"X-Custom-Header": "MyValue"}
      response = api_client.get(f"{httpbin_url}", headers = data)
      data_json = response.json()
      assert response.status_code == 200
      assert  data_json["headers"]["X-Custom-Header"] == "MyValue"

#6
def test_response_headers(api_client, httpbin_base):
    url = (f"{httpbin_base}/response-headers?My-Test-Header=Hello")
    response = api_client.get(url)

    assert response.status_code == 200

    # Validando pelo JSON retornado
    data_json = response.json()
    assert data_json.get("My-Test-Header") == "Hello"

#7
def test_user_agent(httpbin_url, api_client):
      headers_data_user_agent= {"User-Agent": "My-Test-Agent/1.0"}
      data = api_client.get(f"{httpbin_url}", headers = headers_data_user_agent)
      data_user_json = data.json()
      assert data.status_code == 200
      validate_user_header = data_user_json["headers"].get("User-Agent")
      assert validate_user_header == "My-Test-Agent/1.0"

#8

def test_custom_headers(httpbin_url, api_client):
    headers_custom = {"X-Header-1": "Value1", "X-Header-2": "Value2"}

    response = api_client.get(f"{httpbin_url}", headers=headers_custom)
   
    headers_json = response.json()

    assert response.status_code == 200
    assert headers_json["headers"].get("X-Header-1") == "Value1"
    assert headers_json["headers"].get("X-Header-2") == "Value2"

#9

def test_basic_auth(api_client, httpbin_base):
    authenticator = ("user", "passwd")
    response = api_client.get(f"{httpbin_base}/basic-auth/user/passwd", auth=authenticator)
    assert response.status_code == 200
    data_json = response.json()
    assert data_json.get("authenticated") is True
    assert data_json.get("user") == "user"

#10
def test_auth_wrong_password(api_client, httpbin_base):
    authenticator = ("user", "password")
    response = api_client.get(f"{httpbin_base}/basic-auth/user/passwd", auth=authenticator)
    assert response.status_code == 401

#11
def test_valid_bearer_token(api_client, httpbin_base):
    headers_token = {"Authorization": "Bearer my-mock-token"}
    response = api_client.get(f"{httpbin_base}/bearer", headers=headers_token)
    assert response.status_code == 200
    data_json = response.json()
    assert data_json.get("authenticated") is True
    assert data_json.get("token") == "my-mock-token"

#12
def test_without_token(api_client, httpbin_base):
    response = api_client.get(f"{httpbin_base}/bearer")
    assert response.status_code == 401

#13
def test_validate_data_id1(api_client, base_url):
    response = api_client.get(f"{base_url}/users/1")
    data = response.json()
    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    assert isinstance(data["address"], dict)
    assert isinstance(data["company"], dict)

#14
def test_validate_address(api_client, base_url):
    response = api_client.get(f"{base_url}/users/1")
    address = response.json()["address"]
    assert "street" in address
    assert "city" in address
    assert "zipcode" in address

#15
def test_validate_user10(api_client, base_url):
    response = api_client.get(f"{base_url}/posts/10")
    data = response.json()
    assert isinstance(data["userId"], int)
    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert len(data["title"]) > 0
    assert isinstance(data["body"], str)
    assert len(data["body"]) > 0

#16
def test_check_albums(api_client, base_url):
    response = api_client.get(f"{base_url}/photos?albumId=1")
    photos = response.json()
    for photo in photos:
        assert all(k in photo for k in ["albumId", "id", "title", "url", "thumbnailUrl"])

#17
def test_check_email(api_client, base_url):
    response = api_client.get(f"{base_url}/users/3")
    email = response.json()["email"]
    assert "@" in email
    assert "." in email

#18
def test_comments_user_5(api_client, base_url):
    response = api_client.get(f"{base_url}/comments?postId=5")
    comments = response.json()
    assert len(comments) > 0

#19
def test_validate_first_comment_types(api_client, base_url):
    response = api_client.get(f"{base_url}/comments?postId=5")
    first_comment = response.json()[0]
    assert isinstance(first_comment["postId"], int)
    assert isinstance(first_comment["id"], int)
    assert isinstance(first_comment["name"], str)
    assert isinstance(first_comment["email"], str)
    assert isinstance(first_comment["body"], str)

#20
def test_todo_completed_is_boolean(api_client, base_url):
    response = api_client.get(f"{base_url}/todos/199")
    completed = response.json().get("completed")
    assert isinstance(completed, bool)