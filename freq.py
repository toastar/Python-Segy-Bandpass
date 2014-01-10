from numpy import sin, linspace, pi, array, empty
from pylab import plot, show, title, xlabel, ylabel, subplot
from scipy import fft, arange
from obspy.segy.core import readSEGY

filename='test.sgy'; 



def plotSpectrum(y,Fs):
 
 """
 Build a function to Plots the Freq domain
 """
 
 n = len(Data) # length of the signal
 k = arange(n)
 T = n/Fs
 frq = k/T # two sides frequency range
 frq = frq[range(n/2)] # one side frequency range

 Y = fft(y)/n # fft computing and normalization
 Y = Y[range(n/2)]
 
 plot(frq,abs(Y),'r') 
 xlabel('Freq (Hz)')
 ylabel('|Y(freq)|')

# End Function space and begin main section.


segy = readSEGY(filename)   
Data = segy.traces[0].data # This pulls the first trace strips the header and plots a numpy array of the data.

Fs = 250.0;  # sampling rate ( Samples per second.)

datalen = len(Data) #Gets the length of the trace
count = arange(datalen)  
rate = count.astype(float)  / 250.0 # turns sample number into Seconds

# End number crunching and begin buiding plots.

subplot(2,1,1)
plot(rate,Data)
xlabel('Time')
ylabel('Amplitude')
subplot(2,1,2)
plotSpectrum(Data,Fs)
show()

