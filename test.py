"""Example program to show how to read a multi-channel time series from LSL."""

from pylsl import StreamInlet, resolve_stream

Datos=[]
def main():
    # first resolve an EEG stream on the lab network
    print("looking for an EEG stream...")
    streams = resolve_stream('type', 'EEG')

    # create a new inlet to read from the stream
    inlet = StreamInlet(streams[0])

    while True:
        # get a new sample (you can also omit the timestamp part if you're not
        # interested in it)
        sample, timestamp = inlet.pull_sample()
        #print(timestamp, sample)
        Datos.append(sample)
        print(sample)

        if len(Datos)==500:
            break



if __name__ == '__main__':
        main()

print(len(Datos))
print(Datos)