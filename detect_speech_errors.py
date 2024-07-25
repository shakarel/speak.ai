import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import phonetics


def detect_errors(text):
    errors = []

    # Ensure the text is not empty
    if not text.strip():
        errors.append("Empty text provided.")
        return errors

    # Tokenize sentences and process each sentence separately
    sentences = sent_tokenize(text)
    for sentence in sentences:
        sentence = sentence.strip()
        tokens = word_tokenize(sentence)

        # Phonetic error detection
        words = [word.lower() for word in tokens]
        phonetic_errors = detect_phonetic_errors(words)
        errors.extend(phonetic_errors)

    if errors:
        for error in errors:
            print(f"Error: {error}")

    return errors


def detect_phonetic_errors(words):
    phonetic_errors = []
    common_phonetic_mistakes = {
        'TH': ['0NK', '0S', 'TS'],
        'S': ['0S', 'S', 'ZS', 'TS'],
        'B': ['B', 'P', 'BP'],
        'T': ['T', 'D', 'TD'],
        'D': ['D', 'T', 'DT'],
        'K': ['C', 'Q', 'CK']
    }

    for word in words:
        phonetic_code = phonetics.dmetaphone(word)

        # Ensure phonetic_code is not None and has expected structure
        if phonetic_code and len(phonetic_code) == 2:
            for sound, codes in common_phonetic_mistakes.items():
                if (phonetic_code[0] and any(phonetic_code[0].startswith(code) for code in codes)) or \
                        (phonetic_code[1] and any(phonetic_code[1].startswith(code) for code in codes)):
                    phonetic_errors.append(f"Potential mispronunciation detected for word: {word} (sound: {sound})")
                    break

    return phonetic_errors
