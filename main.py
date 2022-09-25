import tkinter as tk

class FindWord:
    def __init__(self, nombre_lettre: int) -> None:
        self.data = self.create_liste()
        self.letters = self.choice_letter(nombre_lettre)

    def create_liste(self) -> list:
        self.liste_mot = []

        with open("lettres/pli07.txt", 'r') as f:
            self.data_liste = f.readlines()

        for line in self.data_liste:
            line = line.strip()
            self.liste_mot.append(line)

        return self.liste_mot

    def choice_letter(self, nombre_lettre: int) -> list:
        self.liste_lettre = []

        for i in range(nombre_lettre):
            self.lettre = input(f"Saisir la lettre {i + 1}: ").upper()
            self.liste_lettre.append(self.lettre)

        return self.liste_lettre

    def is_subseq(self, v2: list, v1: list):
        self.it = iter(v1)
        return all(c in self.it for c in v2)

    def find(self) -> list:
        self.liste_words = []
        for word in self.data:
            self.liste_char = []
            for char in word:
                self.liste_char.append(char)
            self.l1 = sorted(self.letters)
            self.l2 = sorted(self.liste_char)
            self.res = self.is_subseq(self.l2, self.l1)
            if self.res:
                self.liste_words.append(word)

        return self.liste_words


words = FindWord()
mot = words.find()
longest_word = max(mot, key=len)
print(longest_word)
