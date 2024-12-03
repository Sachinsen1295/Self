pip install -r requirements.txt
ollama run llama3



import whisper
from pyannote.audio.pipelines import SpeakerDiarization
from pyannote.core import Segment
from pydub import AudioSegment
import io

# Initialize the ASR model (Whisper)
whisper_model = whisper.load_model("medium")

# Initialize the diarization pipeline
diarization_pipeline = SpeakerDiarization.from_pretrained("pyannote/speaker-diarization",use_auth_token="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")

def diarize_and_transcribe(audio_file):
    # Perform speaker diarization
    diarization = diarization_pipeline({'uri': 'audio', 'audio': audio_file})
    
    # Initialize variables
    transcript = []
    previous_speaker = None
    speaker_segments = {}
    
    # Process each speaker segment and perform transcription using Whisper
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        segment = diarization.get_timeline().crop(turn)
        
        # Extract the audio segment corresponding to the speaker
        start_time = turn.start
        end_time = turn.end
        
        # Load the audio file using pydub
        audio = AudioSegment.from_wav(audio_file)
        
        # Slice the audio for the specific segment
        start_ms = int(start_time * 1000)  # Convert to milliseconds
        end_ms = int(end_time * 1000)
        speaker_audio = audio[start_ms:end_ms]
        
        # Save the sliced audio to a temporary in-memory file
        with io.BytesIO() as temp_audio_file:
            speaker_audio.export(temp_audio_file, format="wav")
            temp_audio_file.seek(0)  # Rewind the file pointer
            # Get the transcription using Whisper for the audio segment
            result = whisper_model.transcribe(temp_audio_file, task="transcribe", language="en", fp16=False)
        
        transcript_text = result['text']
        
        # Storing the speaker and their respective transcript
        if speaker not in speaker_segments:
            speaker_segments[speaker] = []
        
        speaker_segments[speaker].append({
            'segment': Segment(start_time, end_time),
            'transcript': transcript_text
        })
    
    # Prepare the final transcript
    for speaker, segments in speaker_segments.items():
        print(f"Speaker {speaker}:")
        for segment in segments:
            print(f"  [{segment['segment'].start:.2f}s - {segment['segment'].end:.2f}s]: {segment['transcript']}")

# Example usage:
audio_file = 'path_to_audio_file.wav'  # Path to the audio file
diarize_and_transcribe(audio_file)
