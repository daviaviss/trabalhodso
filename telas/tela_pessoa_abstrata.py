from telas.tela_abstrata import TelaAbstrata
from email_validator import validate_email


class TelaPessoaAbstrata(TelaAbstrata):
    def menu_usuario(self):
        print("--- MENU USUARIO ---")
        print("[1] - EDITAR USUARIO")
        print("[2] - EXCLUIR USUARIO")
        print("[0] - VOLTAR")
        opcao = self.le_numero_inteiro("Insira uma das opcoes acima: ", [0, 1, 2])
        return opcao

    def pega_nome_email_usuario(self):
        nome = input("Nome: ")
        email = input("Email: ")
        return {"nome": nome, "email": email}
        

    def valida_email(self, email):
        try:
            validate_email(email)
        except Exception:
            return False
        return True