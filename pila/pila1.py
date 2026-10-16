stack = []
size  = 0
pos = 0

def push(item, stack, size):
    global pos 
    if pos < size:
        stack.append(item)
        pos+=1
    else:
        return "Pila llena..."

def show(stack):
    for item in reversed(stack):
        print(f"|{item}|")


size = int(input("Dime el tamano de la pila: "))

while True:
    item = input("Dime un valor: ")
    print(push(item, stack, size))
    pos+=1
    answer = input("Desea ingresar otro valor [S/N]: ")
    if answer.lower() == "n":
        break

print(show(stack))