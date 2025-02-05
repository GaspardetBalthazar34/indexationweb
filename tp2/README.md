# Indexation et Recherche de Produits

## Description du projet

Ce projet permet d'indexer et de rechercher efficacement des produits à partir d'un fichier `jsonl` contenant des descriptions de produits et leurs avis. L'indexation est réalisée en extrayant les titres, descriptions, caractéristiques (`features`) et avis (`reviews`), pour faciliter la recherche d’informations pertinentes.

## Structure des fichiers

- `main.py` : Script principal qui exécute les différentes étapes du traitement.
- `data_loader.py` : Fonction de chargement des données à partir du fichier `jsonl`.
- `product_processor.py` : Regroupe les variantes et normalise les données des produits.
- `review_processor.py` : Analyse et indexe les avis associés aux produits.
- `index_builder.py` : Crée les index pour les différentes caractéristiques.
- `index_saver.py` : Sauvegarde et charge les index.
- `logger.py` : Gestion des logs dans un fichier externe pour éviter l'affichage tronqué dans le terminal.
- `utils.py` : Fonctions utilitaires pour l’extraction des identifiants produits et variantes.

## Fonctionnalités implémentées

Chargement des produits depuis un fichier `jsonl`.  
Normalisation des produits et de leurs variantes.  
Indexation des titres, descriptions, caractéristiques et avis des produits.  
Calcul des statistiques des avis (moyenne, nombre total et dernière note).  
Sauvegarde et chargement des index en JSON.  
Gestion des logs pour éviter la perte d’informations dans le terminal.  

## Fonctionnalités bonus

Gestion des erreurs et des cas particuliers (produits sans variantes, avis manquants).  
Optimisation des structures de données pour réduire l’espace mémoire utilisé.  

## Exemples d'utilisation

### Exécution du script principal
```bash
python main.py products.jsonl
```

## Format des index générés

Exemple d’index sur les titres :
```json
{
    "box": ["1", "25", "13"],
    "chocolate": ["1", "25", "13"],
    "candy": ["1", "25", "13"]
}
```
```json
Exemple d’index des avis :

{
    "1": {
        "total_reviews": 5,
        "average_rating": 4.6,
        "latest_rating": 4
    }
}
```
## Instructions pour sauvegarder et charger les index

Les index sont sauvegardés sous forme de fichiers JSON :
### Sauvegarde :
```python
from index_saver import save_index
save_index(index_data, "index_output.json")
```

### Chargement :
```python
from index_saver import load_index
index_data = load_index("index_output.json")
```