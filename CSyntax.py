import re
import tkinter as tk

keywords = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']

operators = ['+', '-', '*', '/', '%', '=', '==', '!=', '>', '<', '>=', '<=', '&&', '||', '!', '&', '|', '^', '<<', '>>']

punctuations = [';', ',', '.', '(', ')', '{', '}', '[', ']']

identifier_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'

integer_constant_pattern = r'^[0-9]+$'

floating_point_constant_pattern = r'^[0-9]+\.[0-9]+$'

string_constant_pattern = r'^\".*\"$'

def analyze_code():
    source_code = code_text.get("1.0", "end-1c")

    lines = source_code.split('\n')

    result_text.delete("1.0", "end")

    for line in lines:
        tokens = re.findall(r'\b\w+\b|\S', line)

        is_valid = True

        for token in tokens:
            if token in keywords:
                result_text.insert("end", f'{token} is a keyword\n')
            elif token in operators:
                result_text.insert("end", f'{token} is an operator\n')
            elif token in punctuations:
                result_text.insert("end", f'{token} is a punctuation\n')
            elif re.match(identifier_pattern, token):
                result_text.insert("end", f'{token} is an identifier\n')
            elif re.match(integer_constant_pattern, token):
                result_text.insert("end", f'{token} is an integer constant\n')
            elif re.match(floating_point_constant_pattern, token):
                result_text.insert("end", f'{token} is a floating-point constant\n')
            elif re.match(string_constant_pattern, token):
                result_text.insert("end", f'{token} is a string constant\n')
            else:
                result_text.insert("end", f'{token} is an unknown token\n')
                is_valid = False

        if is_valid:
            result_text.insert("end", f'The line "{line}" is valid\n')
        else:
            result_text.insert("end", f'The line "{line}" is invalid\n')

root = tk.Tk()
root.title("C Code Analyzer")

code_text = tk.Text(root, wrap="word", width=50, height=20)
code_text.pack(padx=10, pady=10)

analyze_button = tk.Button(root, text="Analyze Code", command=analyze_code)
analyze_button.pack(pady=5)

result_text = tk.Text(root, wrap="word", width=50, height=20)
result_text.pack(padx=10, pady=10)

root.mainloop()
