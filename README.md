# Text File Analyzer

This Python project allows a user to analyze a text file and get basic statistics about it, including total lines, total words, total characters, and the most frequent word. It is a console-based application that demonstrates file handling and basic text processing.

## Features
- User can input the filename of a text file.
- Counts total number of lines in the file.
- Counts total number of words in the file.
- Counts total number of characters (including spaces and punctuation).
- Finds and displays the most frequent word along with its occurrence count.

## How to Use
1. Save your text content in a `.txt` file (for example, `sample.txt`).
2. Run the Python script.
3. Enter the name of your text file when prompted.
4. The program will print:
   - Total lines
   - Total words
   - Total characters
   - Most frequent word and its count

## Sample Paragraph for Testing
Python is fun. Python is powerful. Python is easy to learn. Many people love Python because Python is flexible and Python is everywhere.

In this paragraph, the most frequent word is "Python".

## Key Concepts Learned
- Reading files using `open()` and `with` statements.
- User input handling with `input()`.
- Counting lines, words, and characters in a file.
- Using `collections.Counter` to find the most frequent word.
- Basic string processing (splitting, lowercasing).

## Notes
- Make sure the text file is in the same directory as the Python script or provide the full path.
- This project is console-based and does not require any GUI.
