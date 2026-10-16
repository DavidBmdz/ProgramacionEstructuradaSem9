
import speech_recognition as sr

cola = []

def encolar(queue, element):
    queue.append(element)

def desencolar(queue):
    if len(queue) == 0:
        return None
    return queue.pop(0)

def esta_vacia(queue):
    return len(queue) == 0

def mostrar_cola(queue):
    return str(queue)

def escuchar_audio():
    reconocedor = sr.Recognizer()

    with sr.Microphone() as fuente:
        print("Habla ahora... Di un número.")
        reconocedor.adjust_for_ambient_noise(fuente, duration=0.5)

        try:
            audio = reconocedor.listen(
                fuente, timeout=5, phrase_time_limit=5
            )
            texto = reconocedor.recognize_google(
                audio, language="es-ES"
            )
            print("Audio reconocido:", texto)
            return texto

        except sr.WaitTimeoutError:
            print("No se detectó voz a tiempo.")
        except sr.UnknownValueError:
            print("No se pudo entender el audio.")
        except sr.RequestError:
            print("Error de conexión con el servicio de voz.")

        return None

def convertir_elemento(texto):
    if texto is None:
        return None

    texto = texto.strip()

    try:
        return int(texto)
    except ValueError:
        return texto

# Programa principal
while True:
    print("\n--- MENU DE LA COLA ---")
    print("1. Encolar mediante audio")
    print("2. Desencolar")
    print("3. Mostrar cola")
    print("4. Verificar si está vacía")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        elemento = escuchar_audio()

        if elemento is not None:
            elemento = convertir_elemento(elemento)
            encolar(cola, elemento)
            print("Elemento agregado:", elemento)
            print("Cola actual:", mostrar_cola(cola))

    elif opcion == "2":
        elemento = desencolar(cola)

        if elemento is None:
            print("La cola está vacía.")
        else:
            print("Elemento eliminado:", elemento)
            print("Cola actual:", mostrar_cola(cola))

    elif opcion == "3":
        print("Cola actual:", mostrar_cola(cola))

    elif opcion == "4":
        if esta_vacia(cola):
            print("La cola está vacía.")
        else:
            print("La cola contiene elementos.")

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")
