# algoritmo que le idade de uma pessoa expressa em anos, meses e dias e escreve a idade em dias. Considerando o ano 365 dias e mes 30 dias

anos = int(input("\nquantos Anos voce tem?\n"))
meses = int(input("\nquantos meses se passaram desde o seu aniversario?\n"))
dias = int(input("\nquantos dias desse mes se passaram?\n"))

resultado = (anos * 365) + (meses * 30) + dias
print("\n----------------------------------------------------------------\n")
print("\nresultado:\n")
print(f"\nVoce ja viveu {resultado} dias\n\n")