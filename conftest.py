import pytest
import requests
import csv

#Estudar Hook do Pytest

def load_csv_test_cases(path):
    """Reads a CSV file and returns a list of dictionaries."""
    cases = []
    with open(path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cases.append(row)
    return cases


@pytest.fixture(scope="session")
def base_url():
    """Provides the base URL for the API."""
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="function")
def api_client():
    """Provides an API client (requests)."""
    return requests


@pytest.fixture(scope="session")
def httpbin_url():
    """Base URL para testes de headers"""
    return "https://httpbin.org/headers"


@pytest.fixture(scope="session")
def httpbin_base():
    """Base URL para testes"""
    return "https://httpbin.org"

@pytest.fixture(scope="session")
def github_base_url():
    """Base URL da API do GitHub."""
    return "https://api.github.com"


