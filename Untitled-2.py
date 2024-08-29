nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
altura = float(input("Digite a altura (em metros): "))
resultado = (idade > 18) and (altura > 1.75)
msg = f"{nome}, pode participar do evento? {resultado}"
print(msg)