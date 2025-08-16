import random
n1=random.randint(1,20)
n2=0
tentativa=0
while n2 != n1:
    n2 = int(input("Adivinhe um numero: "))
    tentativa += 1
    if n2 > n1:
        print("Mais baixo imbecil")
        print("Vc errou, tente novamente")
    elif n2 < n1:
        print("Mais alto burro")
        print("Vc errou, tente novamente")
if tentativa>5:
    print("demorou pra klr em seu merda ")
elif tentativa<5:
    print("cagada pra klr")

print(f'''Vc acertou em {tentativa} tentativas!''')
    



