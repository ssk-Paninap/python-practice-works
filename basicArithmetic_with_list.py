a = input("input two nums separated by comma: ")
numeros = a.split(',')
n1 = int(numeros[0])
n2 = int(numeros[1])

nsum = n1 + n2
ndiff = n1 - n2
nprod = n1 * n2
nquo = n1 / n2

print(f"sum of {n1} and {n2} is = {nsum}")
print(f"difference {n1} and {n2} is = {ndiff}")
print(f"product of {n1} and {n2} is = {nprod}")
print(f"quotient of {n1} and {n2} is = {nquo}")
