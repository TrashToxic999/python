porta = input("Digite o estado da porta (A para aberta, F para fechada): ").upper()
janela = input("Digite o estado da janela (A para aberta, F para fechada): ").upper()
alarme = (porta == "A") or (janela == "A")
print(f"ALARME DISPARADO - {alarme}")