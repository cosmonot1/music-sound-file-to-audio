import wave as wav
from numpy import fft as FFT
import matplotlib.pyplot as plot

#main runnin of program
if __name__ == "__main__":
	print "Starting program"
	#open text file to convert
	#fName = raw_input( 'Path to input file: ' )
	fName = 'test.txt'
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
	fftData = FFT.fft(data)
	freqData = FFT.fftfreq(len(fftData),1.0/9600)
	print "FFT Completed"

	
	
	

	#TODO: DSP filters to increase or decrease certain frequencies
	print "DSP filters not implemented"
	#fftData2=freqData
	fftData2 =  []
	divisor = 8
	i = 0
	while i<len(freqData):
		if i*divisor<len(freqData):
			fftData2.append(fftData[i*divisor])
		else: 
			fftData2.append(0)
		i += 1
	freqData2 = FFT.fftfreq(len(fftData),1.0/9600)
	print len(freqData2)
	print len(fftData2)
	#how to install plot
	#http://matplotlib.org/faq/installing_faq.html#how-to-install
	#plot.plot(freqData,fftData,'b')
	#plot.plot(freqData2,fftData2,'r')
	#plot.grid()
	#plot.show()
	#exit()

	#inverse fft http://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.ifft.html#numpy.fft.ifft
	#numpy.ifft
	time = FFT.ifft(fftData2)
	print "Inverse FFT completed"
	#Create/open output wav file
	print "Writing to .wav file"
	out = wav.open('out.wav', 'w')
	out.setnchannels(1)
	out.setsampwidth(1)
	out.setframerate(9600)
	for c in time:
		out.writeframes(chr(c))
	print "Wav data written to out.wav"

	#clean up and close all files
	inF.close()
	out.close()
	print "Files saved and closed\n"
	