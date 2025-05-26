nome= input("digite o nome do aluno:")
notas=[]
                 
for i in range(4)   :
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print(F"/nAluno: {nome}")
print("notas:", notas)
print(f"Média::{media:.2f}")

if media>= 50: print("vc foi aprovado")
else:print("vc foi reprovado")
