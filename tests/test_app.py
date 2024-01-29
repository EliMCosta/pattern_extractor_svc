from fastapi.testclient import TestClient
import pytest
from src.main import app  # Ajuste o caminho conforme a organização do seu projeto

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

def test_extrair_entidades(client):
    endpoint = "/extrair-padroes/"
    json_data = {
        "texto": "Meu CPF é 123.456.789-09, PIS 123.45678.12.3, Título 123456789012, CNH 52798802300, e-mail exemplo@dominio.com, CEP 12345-678, nasci em 01/01/1980, tel: (11) 98765-4321, placa ABC1D23.",
        "tipos_labels": [
            "E-mail", "PIS/PASEP", "Outros", "CPF", "CNH"
        ]
    }
    response = client.post(endpoint, json=json_data)

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    data = response.json()
    assert "PIS/PASEP" in data, "PIS/PASEP not found in response"
    assert "52798802300" in data["PIS/PASEP"], "Expected PIS/PASEP '52798802300' not found"
    # Completar mais testes