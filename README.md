# Toy Search Engine

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)

Welcome to **Toy Search Engine**, a lightweight information retrieval system built for educational purposes! This project implements a TF-IDF-based search engine to process and query a corpus of U.S. Inaugural Addresses, showcasing core IR concepts like tokenization, stemming, inverted indexing, and cosine similarity with top-10 optimization.

## ✨ Features

- **Preprocessing**: Tokenizes, stems (Porter Stemmer), and removes stopwords using NLTK
- **TF-IDF Vectorization**: Computes normalized TF-IDF weights for efficient document ranking
- **Inverted Index**: Builds postings lists for fast token-based retrieval
- **Query Processing**: Supports multi-term queries with cosine similarity scoring
- **Top-10 Optimization**: Uses an efficient algorithm to rank documents without full corpus traversal
- **Corpus**: Includes 30 U.S. Inaugural Addresses (1789–1901)

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- NLTK library (`pip install nltk`)
- A directory named `US_Inaugural_Addresses` with 30 `.txt` files (provided or sourced)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Nanduu24/toy-search-engine.git
   cd toy-search-engine
   ```

2. **Install Dependencies**:
   ```bash
   pip install nltk
   python -c "import nltk; nltk.download('stopwords')"
   ```

3. **Prepare Corpus**:
   - Place the 30 U.S. Inaugural Address .txt files in a folder named `US_Inaugural_Addresses` in the project root
   - Ensure filenames match the expected format (e.g., `01_washington_1789.txt`)

4. **Run the Engine**:
   ```bash
   python search_engine.py
   ```

## 📝 Usage

The script runs predefined test cases from CSE 5334 Programming Assignment 1, outputting:

- IDF Values: For tokens "british", "union", "dollar", "constitution", "power"
- TF-IDF Weights: For specific token-document pairs
- Query Results: Top document and score for queries like "executive power"

### Sample Output

```text
Number of documents loaded: 30
30
1.000000000000
0.000000000000
1.000000000000
0.000000000000
0.000000000000
--------------
0.000000000000
0.143507500000
0.152900000000
0.100000000000
0.000000000000
--------------
(17_harrison_1841.txt, 0.310000000000)
(05_jefferson_1805.txt, 0.340000000000)
(03_jefferson_1801.txt, 0.320000000000)
(01_washington_1789.txt, 0.360000000000)
(24_lincoln_1861.txt, 0.330000000000)
```

### Custom Queries

Modify the `__main__` block to test your own queries:

```python
print("(%s, %.12f)" % query("your custom query here"))
```

## 🛠️ How It Works

1. **Preprocessing**:
   - Reads and lowercases text files
   - Tokenizes using RegexpTokenizer(r'[a-z]+')
   - Removes stopwords and stems tokens with Porter Stemmer

2. **TF-IDF Computation**:
   - Builds term frequency (tf) and document frequency (df) tables
   - Computes normalized TF-IDF vectors for each document

3. **Indexing**:
   - Creates sorted postings lists for each token

4. **Query Processing**:
   - Computes TF-IDF for query terms
   - Uses top-10 postings to rank documents via cosine similarity with optimization

## 📚 Project Structure

```text
toy-search-engine/
├── US_Inaugural_Addresses/  # Corpus directory (30 .txt files)
├── search_engine.py         # Main script
└── README.md               # This file
```

## 🌟 Why This Project?

- **Educational**: Demonstrates core IR concepts for CSE 5334 students
- **Lightweight**: No external databases or complex dependencies
- **Extensible**: Easily adaptable for other corpora or enhanced features

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -m "Add new feature"`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- NLTK: For tokenization, stopwords, and stemming tools
- CSE 5334: Inspiration from Programming Assignment 1
- U.S. Presidents: For their eloquent inaugural addresses!

Happy Searching! 🔍

Created with 💻 by Nandu
