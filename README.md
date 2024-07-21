# Audio Steganography Program

This Python program allows you to hide a secret message inside an audio file using the least significant bit (LSB) method. The message is encoded into the audio file in a way that makes it inaudible to the human ear.

## Features
- Encode a secret message into an audio file.
- The output is a modified audio file with the hidden message.
- Uses the least significant bit (LSB) method for encoding.

## Requirements
- Python 3.x
- NumPy

## Installation
1. Clone this repository:
```
https://github.com/William2716057/audioEncryption.git
```
2. Navigate to the project directory:
3. Install the required dependencies:
```
pip install numpy
```
## Usage
To encode a message into an audio file, use the encode_audio function provided in the script. 
```
# Example usage
encode_audio('input.wav', 'output.wav', 'Message to be hidden')
```
Alter the filenames and message to be encrypted
