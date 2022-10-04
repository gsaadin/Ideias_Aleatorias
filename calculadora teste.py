#Fazer uma calculadora
#Receber entrada do primeiro número
#Receber qual/ quais operações que deseja fazer
#Receber segundo número
#Realizar a determinada operação
#Anúnciar resultado
#OBS: evite resultados 2.0, 63.0, 1.0, etc...



print("Calculadora Simples: \n")
a=float(input("Digite seu primeiro número: \n"))

print("Qual operação deseja realizar?\n+ para adicao\n- para subtracao\n* para multiplicacao\n/ para divisao\n** para potenciacao\nr para radiciacao\n// para divisão inteira")
X = input()


b=float(input("Digite seu segundo numero: \n"))
        
#Operações:

if X == "+" :
 print("você selecionou soma\n" "a+b= ", a+b)

if X == "-" :
 print("você selecionou subtracao\n" "a-b= ", a-b)

if X == "*" :
 print("você selecionou multiplicacao\n" "a*b=", a*b)
 
if X == "**" :
 print("você selecionou potenciacao\n" "a**b=", a**b)

if X == "r" :
 print("você selecionou radiciacao\n" "a**(1/b)= ", a**(1/b))

if X == "/" :
 print("você selecionou divisao\n" "a/b=", a/b)

if X == "//" :
 print("você selecionou divisao inteira\n" "a//b=", a//b)

 

elif X != "+" and "-" and "//" and "*" and "**" and "r" and "/":
 print("Desculpa, não entendi o que quis dizer, tente novamente")
 

else:
 print("Fim, obg por usar a calculadora Gsaad!\n VOLTE SEMPRE")

