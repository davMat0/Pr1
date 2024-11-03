import subprocess
import time
import win32clipboard

def descargaArchivo():
    p1 = subprocess.Popen('ftp',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    comandos = [b"verbose\n",
                b"open test.rebex.net\n",
                b"demo\n",
                b"password\n",
                b"get readme.txt\n"]

    for cmd in comandos:
        p1.stdin.write(cmd)
        time.sleep(1)

    respuesta = p1.communicate(timeout=5)[0]

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(respuesta.decode("cp850","ignore"))
    win32clipboard.CloseClipboard()

def comprobarPortapapeles(contenidoAnterior):
    while True:
        win32clipboard.OpenClipboard()
        if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_TEXT):
            contenidoActual = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT).decode("utf-8","ignore")
            if contenidoAnterior != contenidoActual:
                print("EL contenido del portapapeles ha cambiado")
                contenidoAnterior = contenidoActual
        win32clipboard.CloseClipboard()
        time.sleep(1)


if __name__ == "__main__":
    descargaArchivo()

    win32clipboard.OpenClipboard()
    contenido = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT).decode("utf-8","ignore")
    win32clipboard.CloseClipboard()

    comprobarPortapapeles(contenido)



