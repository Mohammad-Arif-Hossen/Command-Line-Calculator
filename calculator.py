import math
import numpy as np
from prompt_toolkit import PromptSession, HTML
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.shortcuts import clear
from colorama import init, Fore, Back, Style as ColorStyle
import re
from typing import List, Dict, Optional
import os
import time
from datetime import datetime

class Calculator:
    def __init__(self):
        self.memory: float = 0
        self.history: List[tuple] = []
        self.last_result: float = 0
        self.variables: Dict[str, float] = {}
        init()  # Initialize colorama
        self.session = PromptSession()
        self.style = Style.from_dict({
            'prompt': '#00aa00 bold',
            'output': '#00aa00',
            'error': '#ff0000',
            'heading': '#00ffff bold',
            'subheading': '#00ffff',
        })

    def print_welcome(self):
        # Clear screen first
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # ASCII Art Logo
        logo = f"""
{Fore.CYAN}
    ██████╗ ██████╗  ██████╗      ██████╗ █████╗ ██╗      ██████╗
    ██╔══██╗██╔══██╗██╔═══██╗    ██╔════╝██╔══██╗██║     ██╔════╝
    ██████╔╝██████╔╝██║   ██║    ██║     ███████║██║     ██║     
    ██╔═══╝ ██╔══██╗██║   ██║    ██║     ██╔══██║██║     ██║     
    ██║     ██║  ██║╚██████╔╝    ╚██████╗██║  ██║███████╗╚██████╗
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝      ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝{ColorStyle.RESET_ALL}
"""
        # Print logo with typing effect
        for char in logo:
            print(char, end='', flush=True)
            time.sleep(0.001)

        # Developer Info and Version
        dev_info = f"""
{Fore.YELLOW}╔══════════════════════════════════════════════════════════════════════════════╗
║  {Fore.CYAN}Developer: {Fore.GREEN}Mohammad Arif Hossen                                              {Fore.YELLOW}║
║                                                          
╚══════════════════════════════════════════════════════════════════════════════╝{ColorStyle.RESET_ALL}
"""
        print(dev_info)

        welcome = f"""
{Fore.CYAN}╔═══════════════════════════════════════════════╗
║          {Fore.YELLOW}Welcome to Pro Calculator{Fore.CYAN}           ║
╠═══════════════════════════════════════════════╣
║ {Fore.YELLOW}Features:{Fore.CYAN}                                    ║
║ ⚡ Math   🔬 Scientific   💾 Memory   📊 History ║
╠═══════════════════════════════════════════════╣
║ {Fore.YELLOW}Quick Guide:{Fore.CYAN}                                 ║
║ 1️⃣ Math: 2 + 2, 5 * 3                         ║
║ 2️⃣ Sci: sin(45), sqrt(16)                     ║
║ 3️⃣ Mem: memory store/recall                   ║
║ ❔ Help: Type 'help'  ❌ Exit: Type 'exit'     ║
╚═══════════════════════════════════════════════╝{ColorStyle.RESET_ALL}
"""
        # Print welcome message with typing effect
        for char in welcome:
            print(char, end='', flush=True)
            time.sleep(0.001)
        print()

        # Show loading animation
        print(f"\n{Fore.GREEN}Initializing system components:", end='', flush=True)
        loading_items = ["Mathematical Engine", "Scientific Functions", "Memory System", "User Interface"]
        for item in loading_items:
            time.sleep(0.3)
            print(f"\n✓ {item}", end='', flush=True)
        print(f"\n\n{Fore.YELLOW}System initialization complete! Ready for calculations.{ColorStyle.RESET_ALL}\n")

    def print_banner(self):
        banner = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════════╗
║                        Pro Calculator                                ║
║                                                                     ║
║    Type {Fore.YELLOW}'help'{Fore.CYAN} for commands  |  Type {Fore.YELLOW}'exit'{Fore.CYAN} to quit              ║
╚══════════════════════════════════════════════════════════════════╝{ColorStyle.RESET_ALL}
"""
        print(banner)

    def format_result(self, result: float) -> str:
        """Format the result with appropriate precision"""
        if isinstance(result, (int, np.integer)):
            return str(result)
        return f"{result:.10g}"

    def evaluate(self, expression: str) -> Optional[float]:
        try:
            # Replace scientific functions with math module equivalents
            expression = expression.lower()
            expression = re.sub(r'sin\((.*?)\)', r'math.sin(math.radians(\1))', expression)
            expression = re.sub(r'cos\((.*?)\)', r'math.cos(math.radians(\1))', expression)
            expression = re.sub(r'tan\((.*?)\)', r'math.tan(math.radians(\1))', expression)
            expression = re.sub(r'log\((.*?)\)', r'math.log10(\1)', expression)
            expression = re.sub(r'ln\((.*?)\)', r'math.log(\1)', expression)
            expression = re.sub(r'sqrt\((.*?)\)', r'math.sqrt(\1)', expression)
            expression = re.sub(r'pi', str(math.pi), expression)
            expression = re.sub(r'e', str(math.e), expression)

            # Handle memory operations
            expression = expression.replace('ans', str(self.last_result))
            
            # Evaluate the expression
            result = eval(expression, {"__builtins__": None}, {
                "math": math,
                "np": np,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "sqrt": math.sqrt,
                "pi": math.pi,
                "e": math.e
            })
            
            return float(result)
        except Exception as e:
            print(f"{Fore.RED}╔══ Error ══╗\n║ {str(e)}\n╚═══════════╝{ColorStyle.RESET_ALL}")
            return None

    def process_command(self, command: str) -> bool:
        command = command.strip().lower()
        
        if command in ['exit', 'quit']:
            print(f"\n{Fore.CYAN}Thanks for using Pro Calculator!{ColorStyle.RESET_ALL}")
            return False
        
        if command == 'help':
            self.show_help()
            return True
            
        if command == 'history':
            self.show_history()
            return True
            
        if command == 'clear':
            os.system('cls' if os.name == 'nt' else 'clear')
            self.print_banner()
            return True
            
        if command.startswith('memory'):
            parts = command.split()
            if len(parts) > 1:
                if parts[1] == 'store':
                    self.memory = self.last_result
                    print(f"{Fore.GREEN}┌─ Memory ─┐\n│ Stored: {self.format_result(self.memory)}\n└──────────┘{ColorStyle.RESET_ALL}")
                elif parts[1] == 'recall':
                    print(f"{Fore.CYAN}┌─ Memory ─┐\n│ Value: {self.format_result(self.memory)}\n└──────────┘{ColorStyle.RESET_ALL}")
                elif parts[1] == 'clear':
                    self.memory = 0
                    print(f"{Fore.GREEN}Memory cleared{ColorStyle.RESET_ALL}")
            return True
            
        result = self.evaluate(command)
        if result is not None:
            self.last_result = result
            self.history.append((command, result))
            print(f"{Fore.GREEN}┌─ Result ─┐\n│ {self.format_result(result)}\n└──────────┘{ColorStyle.RESET_ALL}")
        return True

    def show_help(self):
        help_text = f"""
{Fore.CYAN}╔══════════════════════════════════════════╗
║           Available Commands              ║
╚══════════════════════════════════════════╝{ColorStyle.RESET_ALL}

{Fore.YELLOW}Basic Operations:{ColorStyle.RESET_ALL}
  • Addition:       a + b
  • Subtraction:    a - b
  • Multiplication: a * b
  • Division:       a / b
  • Modulus:        a % b
  • Power:          a ^ b

{Fore.YELLOW}Scientific Functions:{ColorStyle.RESET_ALL}
  • Sine:     sin(x)  [degrees]
  • Cosine:   cos(x)  [degrees]
  • Tangent:  tan(x)  [degrees]
  • Log10:    log(x)
  • Ln:       ln(x)
  • Square root: sqrt(x)

{Fore.YELLOW}Constants:{ColorStyle.RESET_ALL}
  • π (pi):  {math.pi}
  • e:       {math.e}

{Fore.YELLOW}Memory Operations:{ColorStyle.RESET_ALL}
  • memory store  - Store current result
  • memory recall - Recall stored value
  • memory clear  - Clear memory

{Fore.YELLOW}Special Commands:{ColorStyle.RESET_ALL}
  • help    - Show this help
  • history - Show calculation history
  • clear   - Clear screen
  • exit    - Exit calculator
  • ans     - Use previous answer
"""
        print(help_text)

    def show_history(self):
        if not self.history:
            print(f"{Fore.YELLOW}No calculations in history{ColorStyle.RESET_ALL}")
            return
            
        print(f"\n{Fore.CYAN}╔══════════════════════════════════════════╗")
        print(f"║           Calculation History           ║")
        print(f"╚══════════════════════════════════════════╝{ColorStyle.RESET_ALL}\n")
        
        for idx, (expr, result) in enumerate(self.history, 1):
            print(f"{Fore.YELLOW}{idx}.{ColorStyle.RESET_ALL} {expr} {Fore.CYAN}={ColorStyle.RESET_ALL} {self.format_result(result)}")

def main():
    calc = Calculator()
    calc.print_welcome()  # Show welcome screen first
    calc.print_banner()
    
    while True:
        try:
            command = calc.session.prompt(
                HTML(f"<ansigreen>┌─[PRO CALC]</ansigreen>\n└─➤ "),
                style=calc.style
            )
            if not calc.process_command(command):
                break
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit")
            continue
        except EOFError:
            break

if __name__ == "__main__":
    main() 