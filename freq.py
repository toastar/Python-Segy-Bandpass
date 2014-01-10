from numpy import sin, linspace, pi, array, empty, pi
from pylab import plot, show, title, xlabel, ylabel, subplot
from scipy import fft, arange, signal
from obspy.segy.core import readSEGY





#
# Input Parameters Block
#

filename='test.sgy'; 

Lowcut = 8          # Low frequency
Highcut = 60        # High frequency

order = 5           # Higher number means a harsher cutoff


#
#
#





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
rate = -1* count.astype(float)  / 250.0 # turns sample number into Seconds

# End number crunching and begin buiding plots.

subplot(2,2,1)
plot(Data,rate)
ylabel('Time')
xlabel('Amplitude')
subplot(6,1,4)
plotSpectrum(Data,Fs)
show()


#Begin Bandpass

low = Lowcut * 2 / Fs           # 2 / Fs is the nyquest freq / First number is the pass freq
high = Highcut  * 2 / Fs


subplot(2,2,2)                                         

b, a = signal.butter(order, [low,high], btype='band') # Build the filter

BP_Data = signal.lfilter(b, a, Data)                          # Filter Data

plot(BP_Data,rate)                    



subplot(6,1,6)

# Plot Bandpass

#plot(Data[::-1],rate)
ylabel('Time')
xlabel('Amplitude')

plotSpectrum(BP_Data,Fs)

w, h = signal.freqz(b, a, worN=2000)


subplot(6,1,5)
plot((Fs * 0.5 / pi) * w, abs(h))

show()

