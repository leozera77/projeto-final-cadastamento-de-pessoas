import json
import os

ARQUIVO = "pessoas.json"

# Cria o arquivo se não existir
if not os.path.exists(ARQUIVO):
    with open(ARQUIVO, "w") as f:
        json.dump([], f)


def carregar_pessoas():
    with open(ARQUIVO, "r") as f:
        return json.load(f)


def salvar_pessoas(pessoas):
    with open(ARQUIVO, "w") as f:
        json.dump(pessoas, f, indent=4)


def cadastrar_pessoa():
    nome = input("Nome: ").strip()
    idade = input("Idade: ").strip()
    email = input("Email: ").strip()

    pessoa = {
        "nome": nome,
        "idade": idade,
        "email": email
    }

    pessoas = carregar_pessoas()
    pessoas.append(pessoa)
    salvar_pessoas(pessoas)
    print("Pessoa cadastrada com sucesso!\n")


def listar_pessoas():
    pessoas = carregar_pessoas()
    if not pessoas:
        print("Nenhuma pessoa cadastrada.\n")
    else:
        print("\nLista de Pessoas:")
        for idx, p in enumerate(pessoas, 1):
            print(f"{idx}. Nome: {p['nome']} | Idade: {p['idade']} | Email: {p['email']}")
        print("")


def menu():
    while True:
        print("=== Cadastro de Pessoas ===")
        print("1. Cadastrar nova pessoa")
        print("2. Listar pessoas")
        print("3. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_pessoa()
        elif opcao == "2":
            listar_pessoas()
        elif opcao == "3":
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    menu()