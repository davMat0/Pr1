
import subprocess
import asyncio
import time


#funcion que abre notepad de manera sincrona
def showNotepadSincrona():
    try:
        subprocess.run(["notepad.exe"])
    except subprocess.CalledProcessError as e:
        print (e.output)

#funcion que abre notepad de manera asíncrona
async def showNotepadAsincrona():
    try:
        await asyncio.create_subprocess_exec("notepad.exe")
    except subprocess.CalledProcessError as e:
        print (e.output)

async def main():
    continuar = True
    while(continuar):
        print("1-Síncrona\n2.Asíncrona\n0.Salir")
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":#sincrona
            startTime = time.time()
            showNotepadSincrona()
            endTime = time.time()
            print(f"Tiempo de ejecucion síncrona:{(endTime - startTime):.2f}")
        elif opcion == "2":
            startTime = time.time()
            await showNotepadAsincrona()
            endTime = time.time()
            print(f"Tiempo de ejecucion asíncrona:{(endTime - startTime):.2f}")
        elif opcion == "0":
            continuar = False
        else:
            print("la opcion no es correcta")

asyncio.run(main())