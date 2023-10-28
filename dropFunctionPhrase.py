from __future__ import unicode_literals
from polyglot_tokenizer import Tokenizer
import argparse
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def read_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

def write_text_to_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)

def tokenize_and_save(input_file, phrase_list_file, output_file, lang='hi', split_sen=True):
    # Read lines from the input file and join into a single line
    lines = read_lines(input_file)
    single_line_text = ' '.join(lines)

    # Write the single-line output to "singleLineOutput.txt"
    write_text_to_file(single_line_text, "singleLineOutput.txt")
    logging.info("Single line output written to 'singleLineOutput.txt'.")

    # Tokenize the text
    tk = Tokenizer(lang=lang, split_sen=split_sen)
    tokenize_sentences = tk.tokenize(single_line_text)

    # Flatten the nested lists and join sentences with newline
    sentence_output = '\n'.join(' '.join(sentence) for sentence in tokenize_sentences)

    # Save the formatted output to the specified output file
    write_text_to_file(sentence_output, "sentenceOutput.txt")
    logging.info("Tokenized and formatted output written to 'sentenceOutput.txt'.")

    # Read the phrase list
    phrases = read_lines(phrase_list_file)

    # Drop entire multi-word phrases from sentences
    for i, sentence in enumerate(tokenize_sentences):
        for phrase in phrases:
            if ' ' in phrase:
                # If the phrase contains a space, remove the entire multi-word phrase
                sentence = [word for word in sentence if word not in phrase.split()]
            else:
                # If the phrase is a single word, remove that word
                sentence = [word for word in sentence if word != phrase]
        tokenize_sentences[i] = sentence

    # Flatten the nested lists and join sentences with newline for final output
    final_output = '\n'.join(' '.join(sentence) for sentence in tokenize_sentences)

    # Save the formatted output to the specified output file
    write_text_to_file(final_output, output_file)
    logging.info(f"Processed output written to '{output_file}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Drop phrases from sentences and save the result to a file.")
    parser.add_argument("input_file", help="Path to the input file.")
    parser.add_argument("phrase_list_file", help="Path to the phrase list file.")
    parser.add_argument("output_file", help="Path to the output file.")
    parser.add_argument("--lang", default="hi", help="Language code (default: hi).")
    parser.add_argument("--split_sen", default='True', help="Split sentences (default: True).")

    args = parser.parse_args()
    logging.info("Starting tokenization and phrase dropping process...")
    tokenize_and_save(args.input_file, args.phrase_list_file, args.output_file, args.lang, args.split_sen)
    logging.info("Process completed successfully.")
