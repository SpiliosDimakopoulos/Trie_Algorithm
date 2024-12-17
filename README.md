\documentclass[a4paper,12pt]{article}
\usepackage{amsmath}
\usepackage{geometry}
\usepackage{listings}
\geometry{margin=1in}

\title{Word Rectangles Finder}
\author{}
\date{}

\begin{document}

\maketitle

\section*{Overview}
This Python program implements a Trie data structure to efficiently find word rectangles. A word rectangle is a grid of words where all rows and columns are valid words from given word lists.

\section*{Features}
\begin{itemize}
    \item \textbf{Trie Implementation}:
    \begin{itemize}
        \item Insert words into a Trie.
        \item Check if a prefix exists in a Trie.
        \item Print all words stored in the Trie.
    \end{itemize}
    \item \textbf{Word Rectangle Search}:
    \begin{itemize}
        \item Supports finding square word rectangles where rows = columns.
        \item Validates the rectangle using horizontal and vertical word lists.
    \end{itemize}
    \item \textbf{File Input}:
    \begin{itemize}
        \item Reads word lists from files.
    \end{itemize}
    \item \textbf{Command-line Interface}:
    \begin{itemize}
        \item Print Trie contents.
        \item Find word rectangles.
    \end{itemize}
\end{itemize}

\section*{Usage}

\subsection*{1. Print Trie}
Print all words stored in a word list file:
\begin{verbatim}
python word_rectangles.py print_trie <file1>
\end{verbatim}

\textbf{Example:}
\begin{verbatim}
python word_rectangles.py print_trie words.txt
\end{verbatim}

\subsection*{2. Find Word Rectangles}
Find and display word rectangles using horizontal and vertical word lists:
\begin{verbatim}
python word_rectangles.py find_rectangles <file1> <file2> <n_cols>
\end{verbatim}

\begin{itemize}
    \item \texttt{<file1>}: File containing horizontal words (rows).
    \item \texttt{<file2>}: File containing vertical words (columns).
    \item \texttt{<n\_cols>}: Number of columns in the rectangle (also determines the number of rows).
\end{itemize}

\textbf{Example:}
\begin{verbatim}
python word_rectangles.py find_rectangles horizontal.txt vertical.txt 5
\end{verbatim}

\section*{File Format}
Both input files (\texttt{file1} and \texttt{file2}) should contain
