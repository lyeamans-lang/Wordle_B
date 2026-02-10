from pathlib import Path
word_file = Path (" 5-letter-words.txt")

def find_word_file:

return [line.strip().lower() for line in file if len(line.strip()) == 5]
else:

word_file = Path("5-letter-words.txt")

if word_file.exists():
	print("Correct file found")
else:
	print("The file does not exist! :( ")