stack = []
size = 0
pos = 0

def push(item, stack, size):
    if pos < size:
        stack.append(item)
        return "Agregado"
    else:
        return "Pila llena..."

def show(stack):
    for item in reversed(stack):
        print(item)

size = int(input("Dime el tamaño de la pila: "))

while True:
    item = input("Dime un valor: ")
    print(push(item, stack, size))
    pos += 1
    answer = input("Desea ingresar otro valor (S|N): ")
    if answer.lower() == "n":
        break

show(stack)