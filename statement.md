Statement



Problem Statement



Converting decimal numbers to alternative positional numbering systems is a foundational computer science concept, yet learners frequently rely on built-in conversion utilities without grasping the underlying arithmetic mechanisms. 

This project addresses that learning gap by implementing a custom, from-scratch positional conversion system using repeated division and modulus operations, completely bypassing language-level built-ins such as `bin()`, `oct()`, or `hex()`


Scope of the Project 


Supported Inputs         :  Accepts non-negative decimal integers ($N \ge 0$). Negative numbers and non-integer values are out of scope and rejected via continuous validation loops

Supported Bases          :  Fixed standard conversions for base 2 (Binary), base 8 (Octal), and base 16 (Hexadecimal), along with arbitrary custom target bases within the inclusive range of 2 to 16

Interface & Dependencies :  Command-line interface (CLI) execution without external third-party dependencies

 
Target Users


Computer Science & Engineering Students : Beginners learning positional notation, binary arithmetic, and manual base conversion algorithms

Educators                : Instructors seeking clean, modular Python demonstration code that highlights division-remainder logic without reliance on built-in wrappers

Novice Python Developers : Programmers studying clean project modularity (separating entry points, logic, validation, and configuration)


High-Level Features


Repeated Division Algorithm : Converts positive integers and zero using remainder indexing against the symbol set `0123456789ABCDEF`

Standard Base Conversions   : Automatically computes and displays the binary, octal, and hexadecimal equivalents of the user's input

Custom Base Conversion      : Allows dynamic calculation for any selected base between 2 and 16

Robust Input Validation     : Traps non-integer entries and out-of-range base inputs using `try-except` blocks and repeatedly prompts the user until valid inputs are provided

Modular Architecture        : Cleanly isolates configuration (`config.py`), conversion algorithms (`converter.py`), input sanitization (`validation.py`), and application orchestration (`main.py`)
