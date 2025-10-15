# JH_course_genomics

This repository contains my assignments and mini-projects for the *Python for Genomic Data Science* course by Johns Hopkins University on Coursera.

---

## 📘 Project Description

These scripts demonstrate fundamental bioinformatics techniques written in Python — such as calculating GC content, manipulating DNA sequences, and basic genomic data analysis.

This script scans a DNA sequence to identify all potential donor splice site candidates marked by the dinucleotide 'gt'.
It uses Python’s .find() method inside a loop to locate every occurrence and prints their positions.
A flag variable tracks whether any splice sites are found, and if none are detected, the program reports that no donor splice site candidates are present.

All files are stored in the **main** branch and can be run directly using Python 3.  

---

## 🧬 Scripts

- [`gc_content_calculator.py`](gc_content_calculator.py):  
  Calculates the percentage of guanine (G) and cytosine (C) nucleotides in a DNA sequence.
- [`find_donorsplicesite.py`](find_donorsplicesite.py):
  Finds all 'gt' donor splice site candidates in a DNA sequence and prints their positions.
- [`gc_function.py`](gc_function.py):
  Defines a function that computes GC content (%) of a DNA sequence, ignoring ambiguous bases (N).
- [`has_stop_codon.py`](has_stop_codon.py):
  Checks if a DNA sequence contains an in-frame stop codon (TAA, TAG, or TGA) in a user-specified or default reading frame.
- [`reverse_complement.py`](reverse_complement.py):
  Generates the reverse complement of a DNA sequence by reversing and complementing each base (A↔T, C↔G).
- [`dnautil.py`](dnautil.py):
  A Python module that provides functions for DNA sequence analysis, including GC content calculation and detection of in-frame stop codons.
    

  
