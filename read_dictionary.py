import sys

def read_dictionary(path, word_length):
	words = []
	with open(path, "r") as file:
		if 