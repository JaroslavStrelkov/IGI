from standartAnalyzer import StandartTextAnalyzer


from varAnalyzer import VariantAnalyzer



class FullAnalyzer(StandartTextAnalyzer,VariantAnalyzer):

    def __init__(self, text):

        StandartTextAnalyzer.__init__(self, text)

        VariantAnalyzer.__init__(self, text)

    def full_analysis(self):
        result = []
        result.append(f"Количество предложений: " f"{self.count_sentences()}")
        result.append(f"Типы предложений: "f" {self.count_type_sentences()}")
        result.append(f"Средняя длина слова: " f"{self.average_word_length()}")
        result.append(f"Средняя длина предложения: " f"{self.average_sentence_length()}")
        result.append(f"Количество смайлов: " f"{self.smile_count()}")
        result.append(f"Двоичные числа: " f"{self.binary_numbers()}") 
        result.append(f"Слова у которых первая буква гласная, а вторая 2 согласная): " f"{self.vowel_first_list()}")
        result.append(f"Количество слов, начинающихся или заканчивающихся на гласную: " f"{self.start_or_end_vowel()}")
        result.append(f"Частота символов: " f"{self.sym_repeat()}")
        result.append(f"Слова после запятой в алфавитном порядке: " f"{self.word_in_alphabetical_order()}")

        return "\n".join(result)