"""Example program to show how to read a multi-channel time series from LSL."""
from pylsl import StreamInlet, resolve_stream
import csv


Datos=[]

def main():
    print("looking for an EEG stream...")
    streams = resolve_stream('type', 'EEG')
    inlet = StreamInlet(streams[0])
    while True:
        sample, timestamp = inlet.pull_sample()
        Datos.append(sample)
        print(len(Datos))

        if len(Datos)==500:
            with open('DatosPrueba.csv', 'w', newline="") as f:
                writer=csv.writer(f)
                writer.writerows(Datos)
            Datos.clear()
            break



while __name__ == '__main__':
    muestreo=input("Ingresar comando:")
    if muestreo=="a":
        main()

#print(len(Datos))
#print(Datos)