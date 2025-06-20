class Calculator:
    """Classe pour les opérations de calcul de base"""
    
    @staticmethod
    def add(num1: float, num2: float) -> float:
        """Addition de deux nombres"""
        return num1 + num2
    
    @staticmethod 
    def subtract(num1: float, num2: float) -> float:
        """Soustraction de deux nombres"""
        return num1 - num2
    
    @staticmethod
    def multiply(num1: float, num2: float) -> float:
        """Multiplication de deux nombres"""
        return num1 * num2
    
    @staticmethod
    def divide(num1: float, num2: float) -> float:
        """Division de deux nombres"""
        if num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return num1 / num2