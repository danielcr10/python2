# Nome completo: Daniel Cunha Rios
# Matrícula PUC-Rio: 1512920
# Declaração de autoria: Declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.


def entrevista(nEntrevistados):
    totalMulheres = 0
    totalHomens = 0
    mulheresB = 0
    homensB = 0

    for i in range(nEntrevistados):
        print("Bem vindo a pesquisa de mercado sobre os produtos A e B!\n")
        sexo = input("Digite 'F' para sexo feminino e 'M' para masculino: ")
        print("Qual produto voce prefere: 'A' ou 'B'?")
        resp = input("Digite sua resposta: ")
        print("Obrigada por participar!\n")
        if sexo == 'F':
            totalMulheres += 1
            if resp == 'B':
                mulheresB += 1
        else:
            totalHomens += 1
            if resp == 'B':
                homensB += 1

    resultado = (totalMulheres, mulheresB, totalHomens, homensB)
    return resultado


def exibePesquisa(resultado):
    # (totalMulheres, mulheresB, totalHomens, homensB)
    percentMulheres = (100 * resultado[1])/resultado[0]
    percentHomens = (100 * resultado[3])/resultado[2]

    if percentMulheres == percentHomens:
        print("Os homens entrevistados têm a mesma opinião que as mulheres")
    else:
        print("Os homens entrevistados não têm a mesma opinião que as mulheres")
    return


if __name__ == "__main__":
    nEntrev = int(input("Entre com a quantidade de entrevistados: "))
    ret = entrevista(nEntrev)
    exibePesquisa(ret)
