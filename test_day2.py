import requests 
import pytest

#Query Params
#1. Fetch all comments for post ID 2 and verify that all returned comments belong to that post.

def test_comments_id2():
    url= requests.get("https://jsonplaceholder.typicode.com/comments?postId=2")
    response = url.json()
    #print(response)

#2. List all todos for user ID 5 and verify that the list is not empty.

def test_all_user():
     url= requests.get("https://jsonplaceholder.typicode.com/todos?userId=5")
     response = url.json()
     assert url.status_code == 200
     assert response is not None

#3. Fetch all albums for user ID 9 and count how many they have (should be 10).

def test_album():
      url= requests.get("https://jsonplaceholder.typicode.com/albums?userId=9")
      response = url.json()
      assert len(response) == 10
      print(f"O usuario possui {len(response)} albumns")

#4. List all completed todos (completed: true) for user ID 1 and verify that all in the response are indeed completed.

def test_list_all():
       url= requests.get("https://jsonplaceholder.typicode.com/todos?userId=1&completed=true")
       response = url.json()
       assert url.status_code == 200

#Headers
#5. Send a request to httpbin.org/headers with the custom header X-Custom-Header: MyValue and validate the response.

def test_headers():
      url= "https://httpbin.org/headers"
      data = {"X-Custom-Header": "MyValue"}
      data_headers = requests.get(url, headers= data)
      data_json = data_headers.json()
      assert data_headers.status_code == 200
      assert data_json["headers"]["X-Custom-Header"] == "MyValue"

#6. Send a request to httpbin.org/response-headers to set a custom response header (e.g., My-Test-Header: Hello) and check if it is present in the response headers.

def test_response_headers():
    url = "https://httpbingo.org/response-headers?My-Test-Header=Hello"
    
    response = requests.get(url)

    assert response.status_code == 200
    assert response.headers.get("My-Test-Header") == "Hello"



#7. Send a request to httpbin.org/headers with a custom User-Agent header ("My-Test-Agent/1.0") and validate if it was received correctly.

def test_user_agent():
      url = "https://httpbin.org/headers"
      headers_data_user_agent= {"User-Agent": "My-Test-Agent/1.0"}
      data = requests.get(url, headers = headers_data_user_agent)
      data_user_json = data.json()
      assert data.status_code == 200
      validate_user_header = data_user_json["headers"].get("User-Agent")
      assert validate_user_header == "My-Test-Agent/1.0"

#8. Send multiple custom headers (X-Header-1: Value1, X-Header-2: Value2) in a single request to httpbin.org/headers and validate all of them.

def test_custom_headers():
    url = "https://httpbin.org/headers"
    headers_custom = {"X-Header-1": "Value1", "X-Header-2": "Value2"}

    response = requests.get(url, headers=headers_custom)
   
    headers_json = response.json()

    assert response.status_code == 200
    assert headers_json["headers"].get("X-Header-1") == "Value1"
    assert headers_json["headers"].get("X-Header-2") == "Value2"

#Authentication
#9. Test the httpbin Basic Auth endpoint (/basic-auth/user/passwd) with the correct credentials (user, passwd) and validate the 200 status.

def test_basic_auth():
     url = "https://httpbin.org/basic-auth/user/passwd"
     authenticator = ("user", "passwd")

     response = requests.get(url, auth= authenticator)
     assert response.status_code == 200

#10. Test the same Basic Auth endpoint with a correct user but wrong password and validate the 401 status.
def test_auth():
     url = "https://httpbin.org/basic-auth/user/passwd"
     authenticator = ("user", "password")

     response = requests.get(url, auth= authenticator)
     assert response.status_code == 401
     print("Dados incorretos")

#11. Send a request to httpbin.org/bearer with a valid Bearer Token (mock, e.g., "my-mock-token") and validate the successful authentication.

def test_valid_bearer_token():
     url = "https://httpbin.org/bearer"
     headers_token = {"Authorization": "Bearer my-mock-token"}
     authentication = requests.get(url, headers= headers_token)
     assert authentication.status_code == 200
     data = authentication.json()
     assert data["authenticated"] == True
     assert data["token"] == "my-mock-token"

#12. Send a request to httpbin.org/bearer without any authorization header and validate if the response is 401.

def test_without_token():
     url = "https://httpbin.org/bearer"
     #headers_token = {"Authorization": "Bearer "}
     #authentication = requests.get(url, headers= headers_token)
     authentication = requests.get(url)
     assert authentication.status_code == 401
     print("Campo vazio")

#insistance - comparar campo com o tipo (ex:int, str, list)
#Advanced Assertions
#13. Fetch user with ID 1 from JSONPlaceholder and validate the data types of the keys id (int), name (str), address (dict), and company (dict).

def test_validate_data_id1():
     url = "https://jsonplaceholder.typicode.com/users/1"
     response = requests.get(url)
     response_json = response.json()

     assert  isinstance(response_json["id"],int)
     assert  isinstance(response_json["name"],str)
     assert  isinstance(response_json["address"],dict)
     assert  isinstance(response_json["company"],dict)

# For the same user, check if the address key contains the sub-keys street, city, and zipcode.

def test_validate_address():
       url = "https://jsonplaceholder.typicode.com/users/1"
       response = requests.get(url)
       response_json = response.json()
       adress_validate = response_json["address"]

       assert "street" in adress_validate
       assert "city" in adress_validate
       assert "zipcode" in adress_validate

#15. Fetch post with ID 10 and validate if the keys userId and id are integers and if title and body are non-empty strings.

def test_validate_user10():
      url = "https://jsonplaceholder.typicode.com/posts/10"
      response = requests.get(url)
      response_json = response.json()

      assert isinstance (response_json["userId"],int)
      assert isinstance (response_json["id"],int)
      assert isinstance (response_json["title"], str)
      assert  len(response_json["title"]) >0 
      assert isinstance (response_json["body"],str)
      assert  len(response_json["body"]) >0 

#16. List the photos from album with ID 1 and check if each photo in the response contains the keys albumId, id, title, url, and thumbnailUrl.

def test_check_albums():
    url = "https://jsonplaceholder.typicode.com/photos?albumId=1"
    response = requests.get(url)
    response_json = response.json() 

    for photo in response_json:
        assert "albumId" in photo
        assert "id" in photo
        assert "title" in photo
        assert "url" in photo
        assert "thumbnailUrl" in photo

#17. Check if the email key of user with ID 3 follows a valid email format (contains "@" and "." in the domain part).

def test_check_email():
    url = "https://jsonplaceholder.typicode.com/users/3"

    response = requests.get(url)
    response_json = response.json()
    email_json = response_json["email"]

    assert "@" in email_json
    assert "." in email_json

#18. Fetch the comments for post with ID 5 and check if the list of comments is not empty.

def test_comments_user_5():
  url = "https://jsonplaceholder.typicode.com/comments?postId=5"
  response = requests.get(url)
  response_json = response.json()
  response_comments = response_json

  assert len(response_comments) >0

#19. For the first comment from the previous list, validate the types of postId (int), id (int), name (str), email (str), and body (str).

def test_validate_first_comment_types():
    url = "https://jsonplaceholder.typicode.com/comments?postId=5"
    response = requests.get(url)
    response_json = response.json()

    first_comment = response_json[0] 

    assert isinstance(first_comment["postId"], int)
    assert isinstance(first_comment["id"], int)
    assert isinstance(first_comment["name"], str)
    assert isinstance(first_comment["email"], str)
    assert isinstance(first_comment["body"], str)

#20. Fetch the todo with ID 199 and check if the value of the completed key is a boolean (True or False).

def test_todo_completed_is_boolean():
    url = "https://jsonplaceholder.typicode.com/todos/199"
    response = requests.get(url)
    response_json = response.json()

    completed_value = response_json.get("completed")

    assert isinstance(completed_value, bool)
