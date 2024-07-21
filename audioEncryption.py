
import wave
import numpy as np


def encode_audio(audio_file, output_file, message):
    audio = wave.open(audio_file, mode='rb')
    
    #Convert to byte array
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    
    #Append to fill rest of bytes
    message = message + int((len(frame_bytes)-(len(message)*8*8))/8) *'#'
    
    #Convert to bit array
    bits = list(''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in message]))
    
    #Replace least significant bit of each byte of audio data by one bit
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | int(bit)
        
    #Get modified bytes
    frame_modified = bytes(frame_bytes)
    
    #Write modified bytes to new audio file
    with wave.open(output_file, 'wb') as fd:
        fd.setparams(audio.getparams())
        fd.writeframes(frame_modified)
            
    audio.close()
    print("Encoded successfully")
    
encode_audio('input.wav', 'output.wav', 'Message to be hidden')