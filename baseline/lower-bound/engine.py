from translate import Translator
import spacy


class Engine:
    def __init__(self) -> None:
        self.translator = Translator(from_lang="en", to_lang="fr")
        self.nlp = spacy.load("en_core_web_sm")

    def __call__(self, text: str) -> list:
        doc = self.nlp(text)
        result = []
        last_end = 0
        for chunk in doc.noun_chunks:
            if last_end < chunk.start_char:
                result.append(text[last_end : chunk.start_char])

            assert (
                text[chunk.start_char : chunk.end_char] == chunk.text
            ), f'BUG! "{text[chunk.start_char : chunk.end_char]}" != "{chunk.text}"'

            # TODO: separate the annotate-text logic from engine -> move to streamlit_app.py, but don't bother with that now
            result.append((self.translator.translate(chunk.text), text[chunk.start_char : chunk.end_char], "#00d4b133"))
            last_end = chunk.end_char
        if last_end < len(text):
            result.append(text[last_end:])

        return result
