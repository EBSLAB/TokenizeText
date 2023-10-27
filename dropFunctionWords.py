import argparse
from polyglot.text import Text
import re

def join_lines(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return ' '.join(lines)

def tokenize_and_write(input_text, output_file):
    # Tokenize the input text
    tokenized_text = ' '.join([' '.join(sentence.words) for sentence in Text(input_text).sentences])
    # Write the tokenized output to the intermediate file
    with open(output_file, 'w', encoding='utf-8') as intermediate_file:
        intermediate_file.write(tokenized_text)

def split_sentences_and_write(input_file, output_file):
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as input_file:
        input_text = input_file.read()

    # Split the input text into sentences and write each sentence on a new line
    sentences = Text(input_text).sentences
    with open(output_file, 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join([' '.join(sentence.words).replace(' ।', '।') for sentence in sentences]))

def filter_phrases(tokenized_file, phrase_list_file, output_file):
    with open(phrase_list_file, 'r', encoding='utf-8') as phrase_file:
        phrases_to_filter = [phrase.strip().lower() for phrase in phrase_file.readlines()]

    # Read the tokenized file
    with open(tokenized_file, 'r', encoding='utf-8') as tokenized_file:
        tokenized_text = tokenized_file.read()

    # Remove entire phrases from the tokenized text
    for phrase in phrases_to_filter:
        phrase_with_space = f' {phrase} '
        if phrase_with_space in tokenized_text:
            tokenized_text = tokenized_text.replace(phrase_with_space, ' ')

    # Remove multiple spaces
    tokenized_text = re.sub(' +', ' ', tokenized_text)

    # Split the tokenized text into sentences and write each sentence on a new line
    sentences = Text(tokenized_text).sentences
    with open(output_file, 'w', encoding='utf-8') as final_output_file:
        final_output_file.write('\n'.join([' '.join(sentence.words).replace(' ।', '।') for sentence in sentences]))

def main():
    parser = argparse.ArgumentParser(description="Text processing script")
    parser.add_argument("--input_file", required=True, help="Input file containing lines of text.")
    parser.add_argument("--lang", required=True, help="Language for tokenization.")
    parser.add_argument("--word_list_file", required=True, help="File containing a list of phrases or words to filter.")
    parser.add_argument("--output_file", required=True, help="Output file to store the final results.")
    args = parser.parse_args()

    # Step 1: Join lines with newline characters
    text = join_lines(args.input_file)

    # Step 2: Tokenize and write to an intermediate file
    intermediate_file = "singleLineOutput.txt"
    tokenize_and_write(text, intermediate_file)

    # Step 3: Split sentences and write to sentence-level output
    sentence_level_output_file = "sentenceLevelOutput.txt"
    split_sentences_and_write(intermediate_file, sentence_level_output_file)

    # Step 4: Filter phrases or words based on the list
    filter_phrases(intermediate_file, args.word_list_file, args.output_file)

if __name__ == "__main__":
    main()
