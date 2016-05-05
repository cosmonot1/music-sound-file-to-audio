import wave as wav
from numpy import fft as FFT
#import matplotlib.pyplot as plot

#sum two lists together vertically
def verticalSum(l1, l2):
	if len(l1) != len(l2):
		return l1
	else:
		l3=[]
		for i in range(len(l1)):
			l3.append(l1[i] + l2[i])
		return l3

#perform a frequency shift by a ratio of the divisor
def freqShift(data, divisor):
	i = 0
	outData = []
	while i<len(data):
		if i*divisor<len(data):
			outData.append(data[i*divisor])
		else: 
			outData.append(0)
		i += 1
	return outData

#main runnin of program
if __name__ == "__main__":
	print "Starting program"
	#open text file to convert
	#fName = raw_input( 'Path to input file: ' )
	fName = 'in1.txt'
	inF = open( fName, 'r' )

	#read in text file characters
	words = []
	inData = inF.read()
	words = inData.split()
	print "File read"

	#put words into data array
	data = []
	reps = 500
	for w in words:
		for i in range(reps):
			for c in w:
				data.append(ord(c))
	print "Data prepared"

	#fft http://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fft.html#numpy.fft.fft
	#numpy.fft
	fftData = FFT.rfft(data)
	freqData = FFT.rfftfreq(len(fftData),1.0/9600)
	print "FFT completed"

	#TODO: DSP filters to increase or decrease certain frequencies
	#fftData2=freqData
	#shift down the frequencies by a factor of the divisor
	tmp = verticalSum(freqShift(fftData, 4), fftData)
	fftData2 = verticalSum(freqShift(fftData, 2), tmp)
	freqData2 = FFT.rfftfreq(len(fftData),1.0/9600)
	print "DSP filters completed"

	#how to install plot
	#http://matplotlib.org/faq/installing_faq.html#how-to-install
	#plot.plot(freqData,fftData,'b')
	#plot.plot(freqData2,fftData2,'r')
	#plot.grid()
	#plot.show()
	#exit()

	#Inverse FFT
	time = FFT.irfft(fftData2)
	mn = min(time)
	for i in range(len(time)):
		time[i] -= mn
	print "Inverse FFT completed"

	# Create/open output wav file
	print "Writing to .wav file"
	out = wav.open('out1.wav', 'w')
	out.setnchannels(1)
	out.setsampwidth(1)
	out.setframerate(9600)
	for i in range(len(time)):
		if i%(len(time)/10) == 0:
			print "\r  %d%% written" %(i/(len(time)/100)),
		out.writeframes(chr(int(time[i]%256)))
	print "\r  100% written"
	print "Wav data written to out.wav"

	#clean up and close all files
	inF.close()
	out.close()
	print "Files saved and closed\n"
	