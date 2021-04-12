"""Example program to show how to read a multi-channel time series from LSL."""
from pylsl import StreamInlet, resolve_stream
import pandas as pd
import time

DatosBEC = []
DatosBEO = []
DatosLCH = []
DatosRCH = []
DatosLDF = []
DatosLPF = []
DatosRDF = []
DatosRPF = []


BEC = '1'
BEO = '2'
LCH = '3'
RCH = '4'
LDF = '5'
LPF = '6'
RDF = '7'
RPF = '8'

Tipo = 'M'  # Tipos posibles M , I , O
Run = 1
Subject='1'

def mainLCH():
    while True:
        sample, t = inlet.pull_sample()
        DatosLCH.append(sample)
        if len(DatosLCH) == 500:
            df = pd.DataFrame(DatosLCH)
            df.to_csv('DataLCH.csv')
            DatosLCH.clear()
            break


def mainRCH():
    while True:
        sample, t = inlet.pull_sample()
        DatosRCH.append(sample)
        if len(DatosRCH) == 500:
            df = pd.DataFrame(DatosRCH)
            df.to_csv('DataRCH.csv')
            DatosRCH.clear()
            break


def mainLDF():
    while True:
        sample, t = inlet.pull_sample()
        DatosLDF.append(sample)
        if len(DatosLDF) == 500:
            df = pd.DataFrame(DatosLDF)
            df.to_csv('DataLDF.csv')
            DatosLDF.clear()
            break


def mainLPF():
    while True:
        sample, t = inlet.pull_sample()
        DatosLPF.append(sample)
        if len(DatosLPF) == 500:
            df = pd.DataFrame(DatosLPF)
            df.to_csv('DataLPF.csv')
            DatosLPF.clear()
            break


def mainRDF():
    while True:
        sample, t = inlet.pull_sample()
        DatosRDF.append(sample)
        if len(DatosRDF) == 500:
            df = pd.DataFrame(DatosRDF)
            df.to_csv('DataRDF.csv')
            DatosRDF.clear()
            break


def mainRPF():
    while True:
        sample, t = inlet.pull_sample()
        DatosRPF.append(sample)
        if len(DatosRPF) == 500:
            df = pd.DataFrame(DatosRPF)
            df.to_csv('DataRPF.csv')
            DatosRPF.clear()
            break


def mainBEC():
    while True:
        sample, t = inlet.pull_sample()
        DatosBEC.append(sample)
        if len(DatosBEC) == 500:
            df = pd.DataFrame(DatosBEC)
            df.to_csv('DataBEC.csv')
            DatosBEC.clear()
            break


def mainBEO():
    while True:
        sample, t = inlet.pull_sample()
        DatosBEO.append(sample)
        if len(DatosBEO) == 500:
            df = pd.DataFrame(DatosBEO)
            df.to_csv('DataBEO.csv')
            DatosBEO.clear()
            break


print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')
inlet = StreamInlet(streams[0])

while __name__ == '__main__':

    muestreo = input("Ingresar comando:")
    if muestreo == "a":
        mainLCH()
        time.sleep(4)
    elif muestreo == "b":
        mainRCH()
        time.sleep(4)
    elif muestreo == "c":
        mainLDF()
        time.sleep(4)
    elif muestreo == "d":
        mainLPF()
        time.sleep(4)
    elif muestreo == "e":
        mainRDF()
        time.sleep(4)
    elif muestreo == "f":
        mainRPF()
        time.sleep(4)
    elif muestreo == "g":
        mainBEC()
        time.sleep(4)
    elif muestreo == "h":
        mainBEO()
        time.sleep(4)
    else:
        print("Error de comando")
