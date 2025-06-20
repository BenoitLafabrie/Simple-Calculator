import pytest
from unittest.mock import Mock, patch, MagicMock
from src.gui import CalculatorGUI

class TestCalculatorGUI:
    
    @patch('src.gui.Tk')
    def test_gui_initialization(self, mock_tk):
        """Test l'initialisation de l'interface"""
        mock_root = Mock()
        mock_tk.return_value = mock_root
        
        gui = CalculatorGUI()
        
        assert gui.calculator is not None
        assert gui.validator is not None
        mock_root.title.assert_called_with('Python Calculator with Tests')
        mock_root.geometry.assert_called_with('380x300+200+250')
    
    @patch('src.gui.Tk')
    @patch('src.gui.messagebox')
    def test_action_add_valid_numbers(self, mock_messagebox, mock_tk):
        """Test l'addition avec des nombres valides"""
        mock_root = Mock()
        mock_tk.return_value = mock_root
        
        gui = CalculatorGUI()
        gui.entry1 = Mock()
        gui.entry2 = Mock()
        gui.entry1.get.return_value = "5"
        gui.entry2.get.return_value = "3"
        
        # Mock des labels de résultat
        gui.operation_label = Mock()
        gui.result_label = Mock()
        
        gui.action_add()
        
        # Vérifier que le résultat est correct
        gui.result_label.insert.assert_called_with(0, "8")
    
    @patch('src.gui.Tk')
    @patch('src.gui.messagebox')
    def test_action_divide_by_zero(self, mock_messagebox, mock_tk):
        """Test la division par zéro"""
        mock_root = Mock()
        mock_tk.return_value = mock_root
        
        gui = CalculatorGUI()
        gui.entry1 = Mock()
        gui.entry2 = Mock()
        gui.entry1.get.return_value = "10"
        gui.entry2.get.return_value = "0"
        
        gui.action_divide()
        
        # Vérifier qu'une erreur est affichée
        mock_messagebox.showerror.assert_called_once()