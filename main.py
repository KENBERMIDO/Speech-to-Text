"""
Description: This program transcribes recorded speech into readable text.
Usage: Hold 'p' on your keyboard and talk. Let go to stop recording.
"""
import os
import pyaudio
import wave
import keyboard
import whisper

CHUNK = 1024  # number of audio samples per frame
FORMAT = pyaudio.paInt16  # audio format
CHANNELS = 1  # mono audio
RATE = 44100  # sample rate in Hz

program_quit = False
current_dir = os.path.dirname(os.path.abspath(__file__))

transcript_file = os.path.join(current_dir,f'output\\transcript.txt')
output_audio_file = os.path.join(current_dir,f'output\\output_audio.wav')

def record():
    # Create PyAudio object, place it in 'audio'
    audio = pyaudio.PyAudio()

    # Open audio stream from microphone
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("Recording started...")

    # Collect audio data in chunks
    frames = []
    while keyboard.is_pressed('p'):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording finished!")

    # Stop and close audio stream
    stream.stop_stream()
    stream.close()

    # Save audio data to WAV file
    with wave.open(output_audio_file, "wb") as wav_file:
        wav_file.setnchannels(CHANNELS)
        wav_file.setsampwidth(audio.get_sample_size(FORMAT))
        wav_file.setframerate(RATE)
        wav_file.writeframes(b"".join(frames))

def transcribe():
    print("Transcribing speech...")
    model = whisper.load_model("small.en")
    result = model.transcribe(output_audio_file, fp16=False)
    with open(transcript_file, "a") as f:
        print("Captured: ", result["text"])
        f.write(result["text"])

while True:
    print("Hold 'p' on your keyboard to record speech, and let go when you're finished.\n")
    keyboard.wait("p")
    record()
    transcribe()


