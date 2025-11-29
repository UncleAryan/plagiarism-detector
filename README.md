# Plagiarism Detector

A Python program that checks for textual similarity between two documents to identify potential plagiarism. This tool compares user-written content against a source dataset and calculates a similarity percentage.

## Overview

This project implements a simple yet effective plagiarism detection system using Python's built-in `difflib` library. It analyzes the similarity between two text files by comparing sequences and generating a quantitative similarity score.

**Key Features:**
- Compares two text documents for content similarity
- Calculates a percentage-based similarity score
- Provides clear output indicating potential plagiarism levels
- Uses Python's standard library (no external dependencies)

## How It Works

The program leverages `difflib.SequenceMatcher` to analyze the textual similarity between:
- `data-set.txt`: The reference source material
- `plagiarism-check.txt`: The user-submitted text to be verified

The algorithm compares sequences of characters and returns a similarity ratio between 0.0 (completely different) and 1.0 (identical) multiplied by 100 to show readable percentages.

## Requirements

- Python 3 or above

## Usage

1. Place your source text in `data-set.txt`
2. Place the text to be checked in `plagiarism-check.txt`
3. Run the program:
4. View the similarity percentage output in the console

## Example Output
**Sample Output Variations:**
- `The plagiarized content is 15.2%` - Low similarity, likely original content
- `The plagiarized content is 45.8%` - Moderate similarity, review suggested  
- `The plagiarized content is 92.3%` - Very high similarity, potential plagiarism

## Project Structure
.
├── plagiarism-detector.py  # Main program
├── data-set.txt            # Reference source text
├── plagiarism-check.txt    # Text to be verified
└── README.md
