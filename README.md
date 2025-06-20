# Calculatrice Python avec Interface Graphique et CI/CD

Application de calculatrice moderne développée en Python avec interface graphique Tkinter, incluant des tests complets et une intégration continue dans le cadre de mes études en informatique.

## Fonctionnalités

- **Interface Graphique**: Interface utilisateur intuitive développée avec Tkinter
- **Opérations de Base**: Addition, soustraction, multiplication et division
- **Validation des Entrées**: Validation robuste des nombres (entiers, décimaux, négatifs)
- **Gestion d'Erreurs**: Gestion complète des erreurs incluant la protection contre la division par zéro
- **Tests Automatisés**: Couverture de tests complète avec pytest
- **Pipeline CI/CD**: Pipeline Jenkins pour les tests et déploiement automatisés
- **Qualité du Code**: Intégration du linting avec flake8

## Structure du Projet

```
├── src/
│   ├── __init__.py
│   ├── calculator.py      # Logique de calcul
│   ├── gui.py            # Interface graphique
│   └── validator.py      # Utilitaires de validation
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   ├── test_gui.py
│   └── test_validator.py
├── main.py               # Point d'entrée de l'application
├── requirements.txt      # Dépendances Python
├── pytest.ini          # Configuration des tests
├── Jenkinsfile          # Pipeline CI/CD
└── README.md
```

## Prérequis

- **Python 3.9+** : Téléchargeable depuis [python.org](https://www.python.org/downloads/)
- **pip** : Gestionnaire de paquets Python (inclus avec Python)

### Pour le Développement

- **Git** : Système de contrôle de version
- **IDE/Éditeur** : PyCharm, VS Code, ou tout éditeur compatible Python

## Installation

1. **Cloner le dépôt**

   ```bash
   git clone <url-du-depot>
   cd calculatrice-python
   ```

2. **Créer un environnement virtuel**

   ```bash
   python -m venv venv
   ```

3. **Activer l'environnement virtuel**

   **Windows :**

   ```bash
   venv\Scripts\activate
   ```

   **Linux/macOS :**

   ```bash
   source venv/bin/activate
   ```

4. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

### Lancement de l'Application

```bash
python main.py
```

### Exécution des Tests

```bash
# Exécuter tous les tests
pytest

# Tests avec rapport de couverture
pytest --cov=src --cov-report=html

# Exécuter un fichier de test spécifique
pytest tests/test_calculator.py
```

### Vérification du Code

```bash
flake8 src tests --max-line-length=88 --exclude=venv
```

## Interface de l'Application

La calculatrice propose :

- Deux champs de saisie pour les nombres
- Quatre boutons d'opération (+, -, \*, /)
- Affichage du résultat avec opérations color-codées
- Bouton d'informations

### Formats de Nombres Supportés

- Entiers : `123`, `-456`
- Décimaux : `123.45`, `-67.89`
- Décimaux avec point initial : `.123`
- Notation scientifique : `1.23e-4`

## Pipeline CI/CD

Le projet inclut une pipeline Jenkins qui :

1. Récupère le code source
2. Configure l'environnement Python
3. Installe les dépendances
4. Exécute le linting du code
5. Lance tous les tests
6. Génère les rapports de couverture
7. Publie les résultats des tests
8. Envoie des notifications email en cas d'échec

## Tests

Le projet maintient une couverture de tests complète :

- **Tests Unitaires** : Fonctionnalités du calculateur
- **Tests d'Intégration** : Composants de l'interface graphique
- **Tests de Validation** : Logique de validation des entrées
- **Tests de Gestion d'Erreurs** : Scénarios d'exception

## Qualité du Code

- **Linting** : flake8 pour l'application des standards de code
- **Annotations de Type** : Typage statique pour une meilleure documentation
- **Documentation** : Docstrings en français pour toutes les méthodes
- **Gestion d'Erreurs** : Gestion complète des exceptions

## Développement

### Configuration pour le Développement

```bash
# Installer les dépendances de développement
pip install -r requirements.txt

# Exécuter les tests en mode surveillance
pytest --cov=src --cov-report=term-missing -v
```

### Ajout de Nouvelles Fonctionnalités

1. Créer une branche pour la fonctionnalité
2. Implémenter les changements
3. Ajouter des tests pour la nouvelle fonctionnalité
4. S'assurer que tous les tests passent
5. Vérifier le linting du code

## Architecture

L'application suit un pattern d'architecture propre :

- **Modèle** : Classe `Calculator` pour la logique métier
- **Vue** : Classe `CalculatorGUI` pour l'interface utilisateur
- **Validation** : Classe `NumberValidator` pour la validation des entrées
- **Séparation des Responsabilités** : Chaque composant a une responsabilité unique

## Défis Techniques Rencontrés

Durant le développement, j'ai travaillé sur :

- L'intégration de Tkinter pour une interface utilisateur responsive
- L'implémentation de tests unitaires et d'intégration robustes
- La mise en place d'une pipeline CI/CD avec Jenkins
- La gestion des erreurs et validation des entrées utilisateur
- L'application des bonnes pratiques de développement Python

## Améliorations Futures

- Ajout d'opérations mathématiques avancées (puissance, racine carrée)
- Historique des calculs
- Thèmes d'interface personnalisables
- Export des résultats
- Mode calculatrice scientifique
