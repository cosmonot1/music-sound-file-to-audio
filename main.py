import wave as wav
from numpy import fft as FFT
import matplotlib.pyplot as plot

#main runnin of program
if __name__ == "__main__":
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
	freq = FFT.fft(data)
	print "FFT Completed"

	#how to install plot
	#http://matplotlib.org/faq/installing_faq.html#how-to-install
	plot.plot(freq)
	plot.grid()
	plot.show()
	exit()
	

	#TODO: DSP filters to increase or decrease certain frequencies
	print "DSP filters not implemented"

	freq2=[]
	for a in freq:
		if a > 20 and a < 20000:
			freq2.append(a)

	print
	print "MIN:", min(data)
	print "MAX:", max(data)
	print "AVG:", 1.0*sum(data)/len(data)
	print 
	#inverse fft http://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.ifft.html#numpy.fft.ifft
	#numpy.ifft
	time = FFT.ifft(freq2)
	print "Inverse FFT completed"
	
	#Create/open output wav file
	print "Writing to .wav file"
	out = wav.open('out.wav', 'w')
	out.setnchannels(1)
	out.setsampwidth(1)
	out.setframerate(9600)
	for c in data:
		out.writeframes(chr(c))
	print "Wav data written to out.wav"

	#clean up and close all files
	inF.close()
	out.close()
	print "Files saved and closed\n"
	