# TP2 - Moteur de Recherche E-commerce

## 📌 Objectif
Créer des index pour améliorer la recherche de produits e-commerce.

## 📂 Structure du Projet
- `main.py` : Exécute le pipeline complet.
- `data_loader.py` : Charge les données JSONL.
- `indexing.py` : Crée les index pour titres, descriptions, reviews et features.
- `utils.py` : Fonctions utilitaires (préprocessing, logs).
- `output.log` : Fichier de logs des exécutions.

## 🚀 Comment Exécuter
```
python main.py
```

## 📊 Résultats Produits
- **`indexed_output.json`** contient :
  - `index_title`: Index inversé des titres.
  - `index_description`: Index inversé des descriptions.
  - `index_reviews`: Nombre d'avis, moyenne et dernière note.
  - `index_features`: Index des caractéristiques (marque, origine).