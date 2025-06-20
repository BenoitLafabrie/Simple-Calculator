from tkinter import *
from tkinter import messagebox
from .calculator import Calculator
from .validator import NumberValidator

class CalculatorGUI:
    def __init__(self):
        self.calculator = Calculator()
        self.validator = NumberValidator()
        self.setup_ui()
    
    def setup_ui(self):
        """Configuration de l'interface utilisateur"""
        self.root = Tk()
        self.root.title('Python Calculator with Tests')
        self.root.geometry('380x300+200+250')
        self.root.resizable(False, False)
        
        # Titre
        self.title_label = Label(
            self.root, 
            fg='green', 
            font='none 10 bold underline',
            text='Python Calculator', 
            compound=CENTER
        )
        self.title_label.place(relx=0.5, rely=0.1, anchor='center')
        
        # Champs d'entrée
        self.entry1 = Entry(self.root)
        self.entry2 = Entry(self.root)
        self.entry1.place(relx=0.5, rely=0.3, anchor='center')
        self.entry2.place(relx=0.5, rely=0.4, anchor='center')
        
        # Labels de résultat
        self.operation_label = Entry(self.root)
        self.result_label = Entry(self.root)
        
        # Boutons d'opération
        self.setup_buttons()
    
    def setup_buttons(self):
        """Configuration des boutons"""
        Button(self.root, text="+", width=5, 
               command=self.action_add).place(relx=0.1, rely=0.7)
        Button(self.root, text="-", width=5, 
               command=self.action_subtract).place(relx=0.3, rely=0.7)
        Button(self.root, text="*", width=5, 
               command=self.action_multiply).place(relx=0.5, rely=0.7)
        Button(self.root, text="/", width=5, 
               command=self.action_divide).place(relx=0.7, rely=0.7)
        Button(self.root, text='Author', width=6, 
               command=self.show_author).place(relx=0.5, rely=0.95, anchor='center')
    
    def get_numbers(self):
        """Récupère et valide les nombres saisis"""
        num1_str = self.entry1.get().strip()
        num2_str = self.entry2.get().strip()
        
        if not self.validator.is_number(num1_str) or not self.validator.is_number(num2_str):
            raise ValueError("Enter valid numbers\ne.g. 123, 0.123, .123, -0.123, 123.456")
        
        return self.validator.cast_number(num1_str), self.validator.cast_number(num2_str)
    
    def display_result(self, operation: str, result: float, color: str, bg_color: str):
        """Affiche le résultat d'une opération"""
        self.operation_label.delete(0, END)
        self.result_label.delete(0, END)
        
        self.operation_label.config(fg=color, bg=bg_color)
        self.operation_label.insert(0, operation)
        self.operation_label.place(relx=0.5, rely=0.5, anchor='center')
        
        self.result_label.insert(0, str(result))
        self.result_label.place(relx=0.5, rely=0.6, anchor='center')
    
    def action_add(self):
        """Action du bouton addition"""
        try:
            num1, num2 = self.get_numbers()
            result = self.calculator.add(num1, num2)
            self.display_result('Addition', result, 'red', '#9ed8ee')
        except (ValueError, Exception) as e:
            messagebox.showerror("Error", str(e))
    
    def action_subtract(self):
        """Action du bouton soustraction"""
        try:
            num1, num2 = self.get_numbers()
            result = self.calculator.subtract(num1, num2)
            self.display_result('Subtraction', result, 'green', '#ece7e2')
        except (ValueError, Exception) as e:
            messagebox.showerror("Error", str(e))
    
    def action_multiply(self):
        """Action du bouton multiplication"""
        try:
            num1, num2 = self.get_numbers()
            result = self.calculator.multiply(num1, num2)
            self.display_result('Multiplication', result, 'blue', '#cacba9')
        except (ValueError, Exception) as e:
            messagebox.showerror("Error", str(e))
    
    def action_divide(self):
        """Action du bouton division"""
        try:
            num1, num2 = self.get_numbers()
            result = self.calculator.divide(num1, num2)
            self.display_result('Division', result, 'yellow', '#8dad96')
        except (ValueError, ZeroDivisionError, Exception) as e:
            messagebox.showerror("Error", str(e))
    
    def show_author(self):
        """Affiche les informations sur l'auteur"""
        messagebox.showinfo(
            "Author", 
            "Pranta Sarker\nBatch: 6th\nDepartment: CSE\nNorth East University Bangladesh"
        )
    
    def run(self):
        """Lance l'application"""
        self.root.mainloop()
