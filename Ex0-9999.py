print("programa que mostra unidade, dezena, centena e milhar")
num=int(input("Digite um numero entre 0 e 9999 :"))
U= num // 1 % 10 #unidade
D= num // 10 % 10 #dezena
C= num // 100 % 10 #centena
M= num // 1000 % 10 #milhar
print(U)
print(D)
print(C)
print(M)