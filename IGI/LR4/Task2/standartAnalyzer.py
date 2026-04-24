import re
class StandartTextAnalyzer:
    def __init__(self, text):
        self.text = text
    @property
    def text(self):
        return self._text
    @text.setter
    def text(self, value):
        if not isinstance(value, str):
            raise ValueError("Текст должен быть строкой")
        self._text = value

    def count_sentences(self):
        return len(re.findall(r"[.!?]", self.text))
    def count_type_sentences(self):
        res = re.findall(r"[.!?]", self.text)
        return{ res.count("."), res.count("!"), res.count("?")}
    def average_word_length(self):
        words = re.findall(r"\b\w+\b", self.text)
        if words:
            total = sum(len(word) for word in words)
            return round(total/len(words), 2)
        else:
            return 0
        
    def average_sentence_length(self):
        sentences = re.split(r"[.!?]", self.text)
        sentences = [s.strip() for s in sentences]
        if sentences:
            tot = 0
            for sentence in sentences:
                words = re.findall(r"\b\w+\b", sentence)
                tot += sum(len(word) for word in words)
            return round(tot/len(sentences), 2)
        
    def smile_count(self):
        smiles = re.findall(r"[:;]-*[\]\[()]+", self.text)
        return len(smiles)
    
    def __len__(self):
        return len(self.test)
    def __str__(self):
        return f"Текст длинной {len(self)} символов"