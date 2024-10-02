class Pessoa:
    def __init__(self, nome:str, idade: int) -> None:
        self.nome = self._verificar_nome(nome)
        self.idade = self._verificar_idade(idade)

    def _verificar_nome(self, valor):
        self._verificar_nome_tipo_invalido(valor)
        
        self.nome = valor
        return self.nome
    
    def _verificar_idade(self, valor):
        self._verificar_idade_tipo_invalida(valor)
        self._verificar_idade_negativa(valor)
        self._verificar_idade_acima_130(valor)
          
        return self.idade
    
    def _verificar_idade_tipo_invalida(self, valor):
        if not isinstance(valor, int):
            raise TypeError("A idade tem que ser um número inteiro")
        
    def _verificar_idade_negativa(self, valor):
        if valor < 0:
            raise ValueError("A idade não pode ser negativa")
        
    def _verificar_idade_acima_130(self, valor):
        if valor > 130:
            raise ValueError("A idade não pode ser acima de 130")
        self.idade = valor
        
    
    