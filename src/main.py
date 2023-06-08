import pyaudio
import wave
import keyboard
import whisper

# Define constants for recording
CHUNK = 1024  # number of audio samples per frame
FORMAT = pyaudio.paInt16  # audio format
CHANNELS = 1  # mono audio
RATE = 44100  # sample rate in Hz

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

    print("Recording finished...")

    # Stop and close audio stream
    stream.stop_stream()
    stream.close()

    # Save audio data to WAV file
    with wave.open("output.wav", "wb") as wav_file:
        wav_file.setnchannels(CHANNELS)
        wav_file.setsampwidth(audio.get_sample_size(FORMAT))
        wav_file.setframerate(RATE)
        wav_file.writeframes(b"".join(frames))

    print("Saved audio to output.wav")

def transcribe():
    model = whisper.load_model("small")
    result = model.transcribe("output.wav", FP16=False)
    with open("transcript.txt", "w") as f:
        f.write(result["text"])

if __name__ == "__main__":
    record()
    transcribe()
