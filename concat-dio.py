def concat_strings():
    print("Bem-vindo ao ConcatenaFun!")
    strings = []
    
    while True:
        # Recebe a string do usuário
        user_input = input("Digite uma string para adicionar à lista (ou 'sair' para finalizar): ")
        
        if user_input.lower() == 'sair':
            break
        strings.append(user_input)
    
    # Escolha de operação
    print("\nEscolha uma operação de concatenação:")
    print("1: Concatenar sem modificações")
    print("2: Concatenar e inverter cada string")
    print("3: Concatenar com separador personalizado")
    
    choice = input("Digite o número da operação desejada: ")
    
    if choice == '1':
        result = ''.join(strings)
    elif choice == '2':
        result = ''.join(s[::-1] for s in strings)  # Inverte cada string
    elif choice == '3':
        separator = input("Digite o separador que deseja usar: ")
        result = separator.join(strings)
    else:
        print("Escolha inválida! Usando concatenação padrão.")
        result = ''.join(strings)
    
    print(f"\nResultado da concatenação: {result}")

# Chama a função
concat_strings()
