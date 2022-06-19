from abc import ABC

class TelaAbstrata(ABC):


    def mostra_mensagem(self, msg):
        print(msg)


    def le_numero_inteiro(self, msg, inteiros_validos):
        while True:
            opcao = input(msg)
            try:
                opcao = int(opcao)
                if not opcao in inteiros_validos:
                    self.mostra_mensagem("Selecione um dos valores acima!")
                    continue
            except ValueError:
                self.mostra_mensagem("Insira um valor inteiro!")
                continue
            return opcao
    

    def verifica_tipo_dados(self, dados, tipo):
        dados = {
            "int": int ,
            "float": float,
            "dict": dict,
            "list": list
        }
        
        for d in dados:
            try:
                dados[tipo](d)
            except ValueError:
                self.mostra_mensagem("Tipo de dado errado!")
                return False
        return True
        