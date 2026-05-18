#!/usr/bin/env python3
"""
Simple Hangman Game.

How to play:
- The computer randomly selects a word from a list.
- You guess one letter at a time.
- If the letter is in the word, it’s revealed in the correct positions.
- If not, you lose a life.
- The game ends when you guess the word or run out of lives.
"""

import random

WORDS = [
    "python", "computer", "program", "hangman", "challenge", "game", "keyboard",
    "developer", "algorithm", "function", "variable", "iteration", "condition",
    "syntax", "debugger", "exception", "library", "package", "repository",
    "commit", "branch", "merge", "terminal", "console", "network", "database",
    "server", "client", "protocol", "encryption", "security", "performance",
    "scalability", "frontend", "backend", "interface", "graphics", "animation",
    "dataset", "analysis", "machine", "learning", "neural", "battery", "monitor",
    "processor", "storage", "virtual", "container", "orchestration", "cloud",
    "service", "authentication", "authorization", "mobile", "desktop", "widget",
    "pipeline", "automation", "testing", "integration", "deployment", "cache",
    "cookie", "session", "environ", "command", "script", "module", "object",
    "class", "method", "attribute", "syntax", "runtime", "thread", "process",
    "socket", "bandwidth", "latency", "response", "request", "endpoint", "host",
    "domain", "router", "firewall", "proxy"
]


def choose_word():
    return random.choice(WORDS)


def display(word, guessed):
    return " ".join([letter if letter in guessed else "_" for letter in word])


def main():
    print("Welcome to Hangman!\n")
    word = choose_word()
    guessed = set()
    lives = 6

    while lives > 0:
        print(f"Word: {display(word, guessed)}")
        print(f"Lives left: {lives}\n")
        guess = input("Guess a letter or the word: ").strip().lower()

        # check if if its longer than 1 and same length as the word, then check if its correct guess
        if (guess.isalpha() or len(guess) != 1) and len(guess) == len(word):
            if guess.lower() == word:
                print(f"Congratulations! You guessed the word: {word}")
                break
            else:
                lives -= 1
                print("Wrong guess!\n")
                continue
        elif guess.isalpha() and len(guess) == 1:
            print("Please enter a single letter.\n")
            continue

        if guess in guessed:
            print("You already guessed that letter.\n")
            continue

        guessed.add(guess)

        if guess in word:
            print("Good guess!\n")
            if all(letter in guessed for letter in word):
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            lives -= 1
            print("Wrong guess!\n")

    else:
        print(f"Game over! The word was: {word}")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
