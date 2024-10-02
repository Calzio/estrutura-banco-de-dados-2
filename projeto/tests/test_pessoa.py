import pytest
from projeto.models.pessoa import Pessoa

# Boas práticas de programação.

@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa("João", 22)
    return pessoa

def test_pessoa_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "João"
    
def test_pessoa_idade_valida(pessoa_valida):
    assert pessoa_valida.idade == 22
    
def test_pessoa_idade_negativa_retornar_mensagem_erro():
    with pytest.raises(ValueError, match="A idade não pode ser negativa"):
        Pessoa("João", -22)
        
def test_pessoa_idade_acima_130_retornar_mensagem_erro():
    with pytest.raises(ValueError, match="A idade não pode ser acima de 130"):
        Pessoa("João", 131)

def test_pessoa_idade_tipo_invalido_retornar_mensagem_erro():
    with pytest.raises(TypeError, match="A idade tem que ser um número inteiro"):
        Pessoa("João", "22")
        
def test_pessoa_nome_tipo_invalido_retornar_mensagem_erro():
    with pytest.raises(TypeError, match="O nome tem que ser um texto"):
        Pessoa(22, 22)
        
def test_pessoa_nome_vazio_retornar_mensagem_erro():
    with pytest.raises(TypeError, match="O nome não pode ser vazio"):
        Pessoa("", 22)