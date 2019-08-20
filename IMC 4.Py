Altura = 1.74
Peso = 74

IMC = (Peso/Altura**2)
print("Seu IMC é:", IMC)

print("De acordo com o seu IMC:")
print("Você está abaixo do peso", IMC < 18.5)
print("Parabéns, você está com o peso ideal", IMC >= 18.5 and IMC <= 25)
print("Vocẽ está com sobrepeso", IMC >= 25 and IMC < 30)
print("Comece a pensar em atividade física, você está obeso", IMC > 30)