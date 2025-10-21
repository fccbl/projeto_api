from conftest import load_csv_test_cases

def test_create_post_single(base_url, api_client):
    # Lê todos os casos do CSV
    test_cases = load_csv_test_cases("test_cases.csv")

    # Pega o primeiro caso só, para testar manualmente
    test_case = test_cases[0]

    payload = {
        "title": test_case["title"],
        "body": test_case["body"],
        "userId": int(test_case["userId"]) if test_case["userId"] else 1
    }

    response = api_client.post(f"{base_url}/posts", json=payload)
    expected_status = int(test_case["expected_status"])

    # Valida o status e o conteúdo
    assert response.status_code == expected_status
    if expected_status == 201:
        assert response.json()["title"] == payload["title"]

    print("Teste rodou com sucesso!")
