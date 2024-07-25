import os
import nltk
import argparse
from recognize_speech_from_file import recognize_speech_from_file
from recognize_speech_live import recognize_speech_live

# Set the NLTK data path to the directory where I extracted the files
nltk_data_path = os.path.join(os.path.dirname(__file__), 'nltk_data')
nltk.data.path.append(nltk_data_path)

# Ensure the required NLTK data is available
try:
    punkt_path = nltk.data.find('tokenizers/punkt')
    words_path = nltk.data.find('corpora/words')
    tagger_path = nltk.data.find('taggers/averaged_perceptron_tagger')
    print("Found punkt at:", punkt_path)
    print("Found words at:", words_path)
    print("Found averaged_perceptron_tagger at:", tagger_path)
except LookupError as e:
    print(f"Required NLTK data not found: {e}")
    exit()


def main():
    parser = argparse.ArgumentParser(description="Speak.ai CLI for speech error detection.")
    parser.add_argument("--input", type=str, help="Path to the audio file.")
    parser.add_argument("--live", action='store_true', help="Listen to live speech from microphone.")
    args = parser.parse_args()

    if args.live:
        recognize_speech_live()
    elif args.input:
        recognize_speech_from_file(args.input)
    else:
        print("Please provide an audio file with --input or use --live for live speech recognition.")


if __name__ == "__main__":
    main()
