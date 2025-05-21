import json
import os
import statistics

ARQ_USUARIOS = 'usuarios.json'
ARQ_MATERIAS = 'materias.json'

if not os.path.exists(ARQ_USUARIOS):
    f = open(ARQ_USUARIOS, 'w')
    f.write("[]")
    f.close()

if not os.path.exists(ARQ_MATERIAS):
    f = open(ARQ_MATERIAS, 'w')
    json.dump([
        "Python", "TIC", "Sistemas da Informação", "Matemática e Estatística"
    ],
              f,
              indent=4)
    f.close()

f = open(ARQ_USUARIOS, 'r')
usuarios = json.load(f)
f.close()

f = open(ARQ_MATERIAS, 'r')
materias = json.load(f)
f.close()

while True:
    print("\n=== Plataforma Educacional ===")
    print("1 - Se cadastrar")
    print("2 - Login")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        usuario = input("Nome de usuário: ")

        existe = False
        for u in usuarios:
            if u["usuario"] == usuario:
                existe = True
        if existe or usuario == "admin":
            print("Usuário já existe ou é reservado.")
            continue

        while True:
            senha = input("Senha (letras maiúsculas, minúsculas e números): ")
            if (any(c.isupper() for c in senha)
                    and any(c.islower() for c in senha)
                    and any(c.isdigit() for c in senha)):
                break
            else:
                print("Senha fraca. Tente novamente.")

        while True:
            idade_input = input("Idade: ")
            if idade_input.isdigit():
                idade = int(idade_input)
                break
            else:
                print("Idade inválida. Digite apenas números.")

        novo = {
            "usuario": usuario,
            "senha": senha,
            "idade": idade,
            "acessos": 0,
            "materias": []
        }
        usuarios.append(novo)

        f = open(ARQ_USUARIOS, 'w')
        json.dump(usuarios, f, indent=4)
        f.close()

        print("Usuário cadastrado com sucesso.")

    elif opcao == '2':
        login = input("Usuário: ")
        senha = input("Senha: ")

        if login == "admin" and senha == "admin":
            while True:
                print("\n=== MENU ADMIN ===")
                print("1 - Cadastrar nova matéria")
                print("2 - Gerar relatório estatístico")
                print("3 - Voltar")
                op = input("Escolha: ")

                if op == '1':
                    nova_mat = input("Nome da nova matéria: ")
                    if nova_mat in materias:
                        print("Matéria já existe.")
                    else:
                        materias.append(nova_mat)
                        f = open(ARQ_MATERIAS, 'w')
                        json.dump(materias, f, indent=4)
                        f.close()
                        print("Matéria adicionada.")

                elif op == '2':
                    print("\n" + "=" * 40)
                    print("      RELATÓRIO ESTATÍSTICO")
                    print("=" * 40)

                    print("\n" + "-" * 40)
                    print("MÉTRICAS: Idade por matéria")
                    print("-" * 40)
                    for m in materias:
                        idades = []
                        for u in usuarios:
                            if m in u["materias"]:
                                idades.append(u["idade"])
                        if len(idades) > 0:
                            media = statistics.mean(idades)
                            moda = statistics.mode(idades)
                            mediana = statistics.median(idades)
                            print(f"\nMatéria: {m}")
                            print(f"  Média de idade : {media:.2f}")
                            print(f"  Moda de idade  : {moda}")
                            print(f"  Mediana idade  : {mediana}")
                        else:
                            print(f"\nMatéria: {m}")
                            print("  Nenhum aluno matriculado.")

                    print("\n" + "-" * 40)
                    print("MÉTRICAS: Quantidade de matérias por usuário")
                    print("-" * 40)
                    quantidades = [len(u["materias"]) for u in usuarios]
                    if len(quantidades) > 0:
                        print(
                            f"  Média   : {statistics.mean(quantidades):.2f}")
                        print(f"  Moda    : {statistics.mode(quantidades)}")
                        print(f"  Mediana : {statistics.median(quantidades)}")
                    else:
                        print("  Nenhum dado disponível.")

                    print("\n" + "-" * 40)
                    print("MÉTRICAS: Acessos por usuário")
                    print("-" * 40)
                    acessos = [u["acessos"] for u in usuarios]
                    if len(acessos) > 0:
                        print(f"  Média   : {statistics.mean(acessos):.2f}")
                        print(f"  Moda    : {statistics.mode(acessos)}")
                        print(f"  Mediana : {statistics.median(acessos)}")
                    else:
                        print("  Nenhum dado disponível.")
                    print("=" * 40)

                elif op == '3':
                    break
                else:
                    print("Opção inválida.")

        else:
            encontrado = None
            for u in usuarios:
                if u["usuario"] == login and u["senha"] == senha:
                    encontrado = u
            if not encontrado:
                print("Usuário ou senha inválidos.")
                continue

            encontrado["acessos"] += 1
            f = open(ARQ_USUARIOS, 'w')
            json.dump(usuarios, f, indent=4)
            f.close()

            while True:
                print(f"\n=== MENU DE {encontrado['usuario']} ===")
                print("1 - Matricular-se em matéria")
                print("2 - Ver minhas matérias")
                print("3 - Voltar")
                op = input("Escolha: ")

                if op == '1':
                    print("\nMatérias disponíveis:")
                    for i in range(len(materias)):
                        print(f"{i+1} - {materias[i]}")

                    escolha = input("Digite o número da matéria: ")
                    if not escolha.isdigit():
                        print("Entrada inválida.")
                        continue

                    indice = int(escolha) - 1
                    if 0 <= indice < len(materias):
                        materia_escolhida = materias[indice]
                        if materia_escolhida not in encontrado["materias"]:
                            encontrado["materias"].append(materia_escolhida)
                            f = open(ARQ_USUARIOS, 'w')
                            json.dump(usuarios, f, indent=4)
                            f.close()
                            print("Matéria adicionada.")
                        else:
                            print("Você já está nessa matéria.")
                    else:
                        print("Número inválido.")

                elif op == '2':
                    print("\nMinhas matérias:")
                    if encontrado["materias"]:
                        for m in encontrado["materias"]:
                            print("-", m)
                    else:
                        print("Nenhuma matéria cadastrada.")

                elif op == '3':
                    break

                else:
                    print("Opção inválida.")

    elif opcao == '3':
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
