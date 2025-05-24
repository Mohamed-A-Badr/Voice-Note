import environ
from elevenlabs.client import ElevenLabs

env = environ.Env(ELEVENLABS_API_KEY=(str, ""))

client = ElevenLabs(api_key=env("ELEVENLABS_API_KEY"))


def tts(text):
    try:
        audio = client.text_to_speech.convert(
            text=text,
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )

        return audio
    except Exception:
        return None
