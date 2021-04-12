import cv2
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
BEO = '1'
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
    name="S"+Subject+"R"+str(Run)+Tipo+LCH
    im = cv2.imread('C:/Users/Daniel Montoya/Documents/SistemasEmbebidos/OpenbciPrueba/Images/LCH.jpg')
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow("Image", im)
    cv2.waitKey(500)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosLCH.append(sample)
        if len(DatosLCH) == 500:
            cv2.destroyAllWindows()
            df = pd.DataFrame(DatosLCH)
            df.to_csv(name+'.csv')
            DatosLCH.clear()
            break


def mainRCH():
    name="S"+Subject+"R"+str(Run)+Tipo+RCH
    im = cv2.imread('C:/Users/Daniel Montoya/Documents/SistemasEmbebidos/OpenbciPrueba/Images/RCH.jpg')
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow("Image", im)
    cv2.waitKey(500)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosRCH.append(sample)
        if len(DatosRCH) == 500:
            cv2.destroyAllWindows()
            df = pd.DataFrame(DatosRCH)
            df.to_csv(name+'.csv')
            DatosRCH.clear()
            break


def mainLDF():
    name="S"+Subject+"R"+str(Run)+Tipo+LDF
    im = cv2.imread('C:/Users/Daniel Montoya/Documents/SistemasEmbebidos/OpenbciPrueba/Images/LDF.jpg')
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow("Image", im)
    cv2.waitKey(500)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosLDF.append(sample)
        if len(DatosLDF) == 500:
            cv2.destroyAllWindows()
            df = pd.DataFrame(DatosLDF)
            df.to_csv(name+'.csv')
            DatosLDF.clear()
            break


def mainLPF():
    name="S"+Subject+"R"+str(Run)+Tipo+LPF
    im = cv2.imread('C:/Users/Daniel Montoya/Documents/SistemasEmbebidos/OpenbciPrueba/Images/LPF.jpg')
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow("Image", im)
    cv2.waitKey(500)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosLPF.append(sample)
        if len(DatosLPF) == 500:
            cv2.destroyAllWindows()
            df = pd.DataFrame(DatosLPF)
            df.to_csv(name+'.csv')
            DatosLPF.clear()
            break


def mainRDF():
    name="S"+Subject+"R"+str(Run)+Tipo+RDF
    im = cv2.imread('C:/Users/Daniel Montoya/Documents/SistemasEmbebidos/OpenbciPrueba/Images/RDF.jpg')
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow("Image", im)
    cv2.waitKey(500)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosRDF.append(sample)
        if len(DatosRDF) == 500:
            cv2.destroyAllWindows()
            df = pd.DataFrame(DatosRDF)
            df.to_csv(name+'.csv')
            DatosRDF.clear()
            break


def mainRPF():
    name="S"+Subject+"R"+str(Run)+Tipo+RPF
    im = cv2.imread('C:/Users/Daniel Montoya/Documents/SistemasEmbebidos/OpenbciPrueba/Images/RPF.jpg')
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow("Image", im)
    cv2.waitKey(500)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosRPF.append(sample)
        if len(DatosRPF) == 500:
            cv2.destroyAllWindows()
            df = pd.DataFrame(DatosRPF)
            df.to_csv(name+'.csv')
            DatosRPF.clear()
            break


def mainBEC():
    name="S"+Subject+"R"+str(Run)+Tipo+BEC
    #im = cv2.imread('C:/Users/Daniel Montoya/Documents/SistemasEmbebidos/OpenbciPrueba/Images/BEC.jpg')
    #cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    #cv2.imshow("Image", im)
    #cv2.waitKey(500)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosBEC.append(sample)
        if len(DatosBEC) == 500:
            #cv2.destroyAllWindows()
            df = pd.DataFrame(DatosBEC)
            df.to_csv(name+'.csv')
            DatosBEC.clear()
            break


def mainBEO():
    name="S"+Subject+"R"+str(Run)+Tipo+BEO
    #im = cv2.imread('C:/Users/Daniel Montoya/Documents/SistemasEmbebidos/OpenbciPrueba/Images/31262.jpg')
    #cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    #cv2.imshow("Image", im)
    #cv2.waitKey(500)
    inlet = StreamInlet(streams[0])
    while True:
        sample, t = inlet.pull_sample()
        DatosBEO.append(sample)
        if len(DatosBEO) == 500:
            #cv2.destroyAllWindows()
            df = pd.DataFrame(DatosBEO)
            df.to_csv(name+'.csv')
            DatosBEO.clear()
            break


print("looking for an EEG stream...")
streams = resolve_stream('type', 'EEG')
inlet = StreamInlet(streams[0])

while __name__ == '__main__':
        mainLCH()
        time.sleep(4)
        mainRCH()
        time.sleep(4)
        mainLDF()
        time.sleep(4)
        mainLPF()
        time.sleep(4)
        mainRDF()
        time.sleep(4)
        mainRPF()
        time.sleep(4)
        mainBEC()
        time.sleep(4)
        mainBEO()
        time.sleep(4)
        Run+=1



