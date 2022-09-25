import tkinter as tk
from turtle import width


class FindWord:
    def __init__(self, letters: list) -> None:
        self.data = self.create_liste()
        self.letters = letters

    def create_liste(self) -> list:
        self.liste_mot = []

        with open("pli07.txt", 'r') as f:
            self.data_liste = f.readlines()

        for line in self.data_liste:
            line = line.strip()
            self.liste_mot.append(line)

        return self.liste_mot

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


class Gui(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.font = ("Arial", 18)
        self.letters = []

        self.parent.geometry("700x300")
        self.parent.minsize(width=700, height=300)
        self.parent.title("Des lettres et des lettres")
        self.parent.bind('<Return>', self.add_letter)
        self.answer = tk.StringVar()

        self.label = tk.Label(
            self.parent, text="Entrer les lettres puis appuyer sur CHERCHER", font=self.font).pack()
        self.entry = tk.Entry(self.parent, font=self.font, justify="center")
        self.entry.pack()
        self.button = tk.Button(
            self.parent, text="CHERCHER", command=self.search, font=self.font)
        self.button.pack()
        self.button_reset = tk.Button(
            self.parent, text="RESET", font=self.font, command=self.reset)
        self.button_reset.pack()
        self.label_answer = tk.Label(self.parent, font=(
            "Arial", 35), textvariable=self.answer)
        self.label_answer.pack()

    def add_letter(self, event):
        self.letter = self.entry.get().upper()
        self.letters.append(self.letter)
        self.entry.delete(0, 'end')

    def search(self):
        self.words = FindWord(self.letters)
        self.mots = self.words.find()
        self.longest_word = max(self.mots, key=len)
        self.answer.set(self.longest_word)

    def reset(self):
        self.letters = []


if __name__ == '__main__':
    root = tk.Tk()
    Gui(root)
    root.mainloop()
