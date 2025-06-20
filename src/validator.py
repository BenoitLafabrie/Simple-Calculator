class NumberValidator:
    """Classe pour la validation des entrées numériques"""
    
    @staticmethod
    def is_number(s: str) -> bool:
        """Vérifie si une chaîne représente un nombre valide"""
        if not s or s.isspace():
            return False
            
        s = s.strip()
        
        try:
            float(s)
            return True
        except ValueError:
            return False
    
    @staticmethod
    def cast_number(num_str: str) -> float:
        """Convertit une chaîne en nombre (int ou float)"""
        if not NumberValidator.is_number(num_str):
            raise ValueError(f"'{num_str}' is not a valid number")
        
        num_str = num_str.strip()
        
        # Retourne int si c'est un entier, sinon float
        if '.' not in num_str:
            try:
                return int(num_str)
            except ValueError:
                pass
        
        return float(num_str)