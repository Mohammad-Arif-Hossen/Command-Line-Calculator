# Pro Command Line Calculator

A professional-grade command-line calculator with advanced mathematical capabilities and a modern UI.

<div align="center">

![Developer](https://img.shields.io/badge/Developer-Mohammad%20Arif%20Hossen-blue)
![Version](https://img.shields.io/badge/Version-1.0.0-green)
![Python](https://img.shields.io/badge/Python-3.8+-yellow)
![License](https://img.shields.io/badge/License-MIT-red)

</div>

## ✨ Features

- 🔢 **Basic Operations**
  - Addition, Subtraction, Multiplication, Division
  - Modulus and Power operations
  - Support for parentheses and complex expressions

- 🔬 **Scientific Functions**
  - Trigonometric: sin, cos, tan (in degrees)
  - Logarithmic: log (base 10), ln (natural log)
  - Square root and other mathematical functions
  - Mathematical constants (π, e)

- 💾 **Memory Management**
  - Store current result
  - Recall stored value
  - Clear memory function

- 📊 **Additional Features**
  - Calculation history tracking
  - Customizable precision
  - Modern command-line interface
  - Color-coded output
  - Interactive help system

## 🚀 Requirements

- Python 3.8 or higher
- Required packages:
  ```
  prompt_toolkit>=3.0.38
  colorama>=0.4.6
  numpy>=1.24.0
  ```

## 📥 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Mohammad-Arif-Hossen/Command-Line-Calculator.git
   cd pro-calculator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. For Linux/Mac users, make the run script executable:
   ```bash
   chmod +x run.sh
   ```

## 💻 Usage

There are two ways to run the calculator:

1. **Quick Start**: 
   - **Windows**: Double-click `run.cmd` or run:
     ```bash
     run.cmd
     ```
   - **Linux/Mac**: Double-click `run.sh` or run:
     ```bash
     ./run.sh
     ```

2. **Manual Start (All Platforms)**:
   ```bash
   python calculator.py
   ```

### 🎯 Quick Start Guide

1. Basic calculations:
   ```
   calc ➤ 2 + 2
   = 4
   ```

2. Scientific functions:
   ```
   calc ➤ sin(90)
   = 1
   calc ➤ sqrt(16)
   = 4
   ```

3. Using memory:
   ```
   calc ➤ 100
   = 100
   calc ➤ memory store
   calc ➤ memory recall
   = 100
   ```

### 🛠️ Available Commands

- `help` - Display available commands and functions
- `history` - Show calculation history
- `clear` - Clear screen
- `exit` or `quit` - Exit calculator
- `memory store` - Store current result
- `memory recall` - Recall stored value
- `memory clear` - Clear stored value
- `ans` - Use previous answer in calculation

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/Mohammad-Arif-Hossen/Command-Line-Calculator).

## 📝 License

This project is [MIT](LICENSE) licensed.

## 👨‍💻 Developer

**Mohammad Arif Hossen**
- GitHub: [@yourusername](https://github.com/Mohammad-Arif-Hossen) 
