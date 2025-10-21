from conftest import load_csv_test_cases

def test_csv_data():
    # Lê todos os casos do CSV
    test_cases = load_csv_test_cases("test_cases.csv")

    # Testa cada linha
    for test_case in test_cases:
        # Verifica se os campos existem
        assert "title" in test_case
        assert "body" in test_case
        assert "userId" in test_case
        assert "expected_status" in test_case

        # Verifica tipos e valores simples
        assert isinstance(test_case["title"], str)
        assert isinstance(test_case["body"], str)
        # userId pode estar vazio, então só verifica se é int ou vazio
        if test_case["userId"]:
            assert test_case["userId"].isdigit()
        # expected_status deve ser numérico
        assert test_case["expected_status"].isdigit()
