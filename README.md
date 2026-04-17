# COMP2152 — Open Source Development Labs
### George Brown Polytechnic · School of Computer Technology

A collection of weekly Python lab assignments completed as part of the **COMP2152 Open Source Development** course at George Brown Polytechnic (Toronto, ON).

---

## About the Course

COMP2152 covers practical Python development with a focus on open source tools, software design principles, and real-world scripting. Topics span core Python fundamentals through to networking, data structures, algorithms, and security concepts.

---

## Repository Structure

```
COMP2152_Labs/
├── Week01/       # Python basics — variables, data types, I/O
├── Week02/       # Control flow — conditionals and loops
├── Week03/       # Functions and scope
├── Week04/       # Lists and tuples
├── Week05/       # Dictionaries and sets
├── Week06/       # File I/O and exception handling
├── Week09/       # Object-oriented programming
├── Week10/       # Modules and packages
├── Week11/       # Algorithms — searching and sorting
├── Week13/       # Data structures
├── Week14/       # Networking and security
│   ├── Q1.py     # [Week 14 Q1]
│   └── Q2.py     # HTTP Security Header Checker
├── assignments/  # Graded assignments
├── binary_search.py
├── dijkstra.py
├── ferry.py
└── README.md
```

---

## Highlights

### `Week14/Q2.py` — HTTP Security Header Checker
Scans a target URL and audits for the presence of key HTTP security headers:

| Header | Purpose |
|---|---|
| `Content-Type` | Prevents MIME ambiguity |
| `X-Frame-Options` | Protects against clickjacking |
| `X-Content-Type-Options` | Blocks MIME sniffing |
| `Strict-Transport-Security` | Enforces HTTPS |
| `Content-Security-Policy` | Mitigates XSS attacks |
| `X-XSS-Protection` | Browser-level XSS filter |

### `dijkstra.py`
Implementation of Dijkstra's shortest-path algorithm.

### `binary_search.py`
Binary search implementation with iterative and/or recursive approaches.

### `ferry.py`
A simulation or scheduling script — ferry boarding/ticketing logic.

---

## Getting Started
'''
Mkdir
Clone repo

**Run any script:**
```bash
python Week14/Q2.py
```

**Requirements:**
- Python 3.x
- Standard library only (no external packages required for most scripts)

---

## Author

**Bastian** · George Brown Polytechnic  
COMP2152 — Open Source Development

## Teacher

**Barty Crouch** **M_Sojoudian**
---

*Lab work completed across 14 weeks. Each week's folder contains one or more `.py` files corresponding to in-class lab questions.*