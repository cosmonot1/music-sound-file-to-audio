import wave as wav
from numpy import fft as FFT

#main runnin of program
if __name__ == "__main__":
	#open text file to convert
	#fName = raw_input( 'Path to input file: ' )
	fName = 'test.txt'
	inF = open( fName, 'r' )

	#read in text file data
	data = []
	while True:
		c = inF.read(1)
		if c:
			c = ord( c[0] )
			data.append(c)
		else:
			print "File read"
			break

	#TODO: FFT
	print "FFT not implemented"
	#fft http://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fft.html#numpy.fft.fft
	#numpy.fft
	print data[0:10]
	freq = FFT.fft(data)
	print len(freq)

	#TODO: DSP filters to increase or decrease certain frequencies
	print "Filters not implemented"

	#TODO: Inverse FFT
	#inverse fft http://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.ifft.html#numpy.fft.ifft
	#numpy.ifft
	print "Inverse FFT not implemented"
	time = FFT.ifft(freq)
	print time[0:10]
	
	#Create/open output wav file
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
	print "Files saved and closed"
	print "Exiting\n"