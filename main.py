import wave as wav

'''
a = wav.open('test.wav', 'r')
b = wav.open('out.wav', 'w')
b.setnchannels(1)
b.setsampwidth(1)
b.setframerate(9600)
for d in range(100):
	b.writeframes('01234567890abcdefghijklmnopqrstuvwxyz \
	ABCDEFGHIJKLMNOPQRSTUVXYZ`~!@#$%^&*()_+-=\\|;\'",./<>?')
a.close()
b.close()
'''

#open text file you want to turn into sound
#read in text file line by line or byte by byte or w/e
#do FFT
#DSP certain frequencies
#do inverse FFT
#write to file