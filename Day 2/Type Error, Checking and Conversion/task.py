# A função len() não aceita números inteiros puros. Se descomentarmos a linha abaixo, o Python vai acusar um TypeError:
# len(12345)

# Como colocamos as aspas, o Python enxerga como um texto (String). O len() vai contar que há 5 caracteres aqui:
len("12345")

# Conta e devolve quantas letras tem na palavra (resultado seria 5):
len("Hello")

# A função type() investiga a "natureza" do dado. Aqui, ela revela ao print que "Hello" é uma String (str):
print(type("Hello"))

# Investiga e revela que 123 é um número inteiro (int):
print(type(123))

# O underline é apenas visual para nós, humanos. O type() revela que continua sendo um número inteiro (int):
print(type(123_456_789))

# Como tem um ponto decimal, o type() revela que é um Float (número de ponto flutuante):
print(type(123.8909))

# Sendo um valor lógico de Verdadeiro ou Falso, o type() revela que é um Booleano (bool):
print(type(True))

# Make this line of code run without errors

name_of_the_user = input("Enter your name")

length_of_name = len(name_of_the_user)

# O Python não permite concatenar (juntar com +) um texto com um número:
print("Number of letters in your name: " + str(length_of_name))