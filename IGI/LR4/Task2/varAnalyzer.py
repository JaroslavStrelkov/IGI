import re
class VariantAnalyzer:
    vowels = "аеёиоуыэюяaeiou"
    def __init__(self, text):
        self.text = text
    def binary_numbers(self):
        return re.findall(r"\b[01]+\b", self.text)
    def vowel_first_list(self):
        return re.findall(r"\b[аеёиоуыэюяaeiou]"r"[^аеёиоуыэюяaeiou\W]\w*\b", self.text, re.IGNORECASE)
    def start_or_end_vowel(self):
        words = re.findall(r"\b\w+\b", self.text)
        count = 0
        for word in words:
            if word[0].lower() in self.vowels or word[-1].lower() in self.vowels:
                count += 1
        return count
    def sym_repeat(self):
        repeat = {}
        for sym in self.text:
            repeat[sym] = repeat.get(sym, 0) + 1
        return repeat
    
    def word_in_alphabetical_order(self):
        return sorted(re.findall(r",\s*([А-Яа-яA-Za-z]+)",self.text))


