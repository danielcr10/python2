#Nome completo: Daniel Cunha Rios
#Matrícula PUC-Rio: 1512920
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim, sem consultas a outros alunos, professores ou qualquer outra pessoa.

def exibeMomentoMatricula(dCursos, dAprovados):
  horarios = ('8h às 9:30h', '10h às 11:30h', '13h às 14:30h', '15h às 16:30h', '17h às 18:30h')

  for key in dAprovados:
    nome = key
    curso = dAprovados[key][0]
    coloc = dAprovados[key][1]
    dia = dCursos[curso][0]
    tVagas = dCursos[curso][1]
    vagaHorario = tVagas/5
    
    for i in range(1,5):
      if coloc <= vagaHorario * i:
        horario = horarios[i-1]
        break

    print("nome: {} \t curso: {} \t dia: {} \t horário: {}".format(nome, curso, dia, horario))




dCursos={'engenharia':('5/01/2018',550),'direito':('6/01/2018',350),
'economia':('7/01/2018',160),'design':('8/01/2018',240)}
dAprovados={'Ana':('economia',75),'Jose':('engenharia',399),'Joao':('direito',5)}

exibeMomentoMatricula(dCursos, dAprovados)
