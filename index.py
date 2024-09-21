import csv

def calcular_area_retangulo(comprimento, largura):
    return comprimento * largura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_insumos(area, quantidade_por_metro):
    return area * quantidade_por_metro

dados = []

def mostrar_menu():
    print("\nMenu de Opções:")
    print("1. Inserir dados")
    print("2. Atualizar dados")
    print("3. Deletar dados")
    print("4. Mostrar dados")
    print("5. Sair")

def inserir_dados():
    escolha = int(input("Escolha a cultura: 1 - Milho, 2 - Soja: "))
    
    if escolha == 1:
        print("Você escolheu Milho (Área como Retângulo).")
        escolha_escrita = "Milho"
        comprimento = float(input("Digite o comprimento do campo (em metros): "))
        largura = float(input("Digite a largura do campo (em metros): "))
        area = calcular_area_retangulo(comprimento, largura)
        quantidade_por_metro = float(input("Digite a quantidade de insumo por metro quadrado: "))
        insumo = calcular_insumos(area, quantidade_por_metro)
    elif escolha == 2:
        print("Você escolheu Soja (Área como Triângulo).")
        escolha_escrita = "Soja"
        base = float(input("Digite a base do campo (em metros): "))
        altura = float(input("Digite a altura do campo (em metros): "))
        area = calcular_area_triangulo(base, altura)
        quantidade_por_metro = float(input("Digite a quantidade de insumo por metro quadrado: "))
        insumo = calcular_insumos(area, quantidade_por_metro)
    else:
        print("Opção inválida.")
        return
    
    value = {
        "id": len(dados) + 1,
        "cultura": escolha_escrita,
        "area": area,
        "insumo": insumo
    }
    
    dados.append(value)
    print(f"Área calculada: {area} metros quadrados")
    print(f"Insumo necessário: {insumo} litros")

def atualizar_dados():
    id_especifico = int(input("Digite o id dos dados a serem atualizados: "))
    
    try:
        dado_filtrado = next((item for item in dados if item['id'] == id_especifico), None)
        
        if dado_filtrado is None:
            print(f"ID {id_especifico} não encontrado.")
            return
        
        print(f"Dado atual antes da atualização: {dado_filtrado}")
        
        escolha = int(input("Escolha a cultura: 1 - Milho, 2 - Soja: "))
    
        if escolha == 1:
            print("Você escolheu Milho (Área como Retângulo).")
            escolha_escrita = "Milho"
            comprimento = float(input("Digite o comprimento do campo (em metros): "))
            largura = float(input("Digite a largura do campo (em metros): "))
            area = calcular_area_retangulo(comprimento, largura)
            quantidade_por_metro = float(input("Digite a quantidade de insumo por metro quadrado: "))
            insumo = calcular_insumos(area, quantidade_por_metro)
        elif escolha == 2:
            print("Você escolheu Soja (Área como Triângulo).")
            escolha_escrita = "Soja"
            base = float(input("Digite a base do campo (em metros): "))
            altura = float(input("Digite a altura do campo (em metros): "))
            area = calcular_area_triangulo(base, altura)
            quantidade_por_metro = float(input("Digite a quantidade de insumo por metro quadrado: "))
            insumo = calcular_insumos(area, quantidade_por_metro)
        else:
            print("Opção inválida.")
            return

        dado_filtrado['cultura'] = escolha_escrita
        dado_filtrado['area'] = area
        dado_filtrado['insumo'] = insumo

        print("Dados atualizados com sucesso.")
        print(f"Dado atualizado: {dado_filtrado}")
    
    except Exception as e:
        print(f"Falha ao atualizar. Erro: {e}")

def deletar_dados():
    global dados 
    id = int(input("Digite o id dos dados a serem deletados : "))
    try:
        dados = [item for item in dados if item['id'] != id]
        print("Excluído com sucesso")
    except Exception as e:
        print(f"Erro ao excluir dados: {e}")

def mostrar_dados():
    if len(dados) == 0:
        print("Nenhum dado disponível.")
    else:
        for i in dados:
            id = i["id"]
            cul = i["cultura"]
            are = i["area"]
            ins = i["insumo"]
            print(f"""
                Id = {id}
                Cultura = {cul}
                Área = {are} metros quadrados
                Insumo necessário = {ins}L

                -------------------------------------------- \n
            """)

def salvar_dados_csv(nome_arquivo):
    with open(nome_arquivo, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "cultura", "area", "insumo"])
        for dado in dados:
            writer.writerow([dado['id'], dado['cultura'], dado['area'], dado['insumo']])
    print(f"Dados salvos no arquivo {nome_arquivo}")

while True:
    mostrar_menu()
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        inserir_dados()
        salvar_dados_csv("dados_agricultura.csv")
    elif opcao == 2:
        atualizar_dados()
        salvar_dados_csv("dados_agricultura.csv")
    elif opcao == 3:
        deletar_dados()
        salvar_dados_csv("dados_agricultura.csv")
    elif opcao == 4:
        mostrar_dados()
    elif opcao == 5:
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida.")
