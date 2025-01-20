# NBA player statistics analysis

### **Projet : Prédiction des performances des joueurs de basket en fonction de leurs statistiques**

**Objectif :**  
Créer un modèle de machine learning capable de prédire les performances futures d’un joueur de basket (par exemple, le nombre de points, rebonds, passes décisives par match) en fonction de ses statistiques passées et d'autres facteurs (minutes jouées, position, adversaire, etc.). Accompagne cela de visualisations impactantes pour analyser les résultats.

---

### **Étapes du projet :**

#### 1. **Collecte de données :**
- Récupère des données de basket-ball via des APIs ou des sources en ligne comme :
  - [Basketball Reference](https://www.basketball-reference.com/)
  - [Kaggle Datasets](https://www.kaggle.com/)
  - [NBA API](https://github.com/swar/nba_api)
- Les données doivent inclure :
  - Les statistiques des joueurs (points, rebonds, passes décisives, etc.)
  - Les données contextuelles (date du match, adversaire, minutes jouées, position, etc.)
  - Les performances d'équipe (victoire/défaite, score total, etc.)

---

#### 2. **Exploration des données :**
- Nettoie les données (traitement des valeurs manquantes, gestion des doublons, etc.).
- Fais une analyse exploratoire des données (EDA) pour comprendre les relations entre les variables.
- Crée des visualisations avec **Matplotlib**, **Seaborn**, ou **Plotly** :
  - Histogrammes pour les statistiques des joueurs.
  - Heatmaps pour les corrélations.
  - Graphiques temporels pour suivre les performances sur la saison.

---

#### 3. **Feature Engineering :**
- Crée des variables supplémentaires, par exemple :
  - Forme récente d’un joueur (moyenne des 5 derniers matchs).
  - Impact de l’adversaire (défense moyenne de l’équipe adverse).
  - Position spécifique du joueur (poste 1 à 5).

---

#### 4. **Construction du modèle :**
- Teste différents modèles de machine learning :
  - **Régression linéaire** : Pour prédire les points par match.
  - **Arbres de décision** ou **Random Forest** : Pour capturer des relations complexes.
  - **Réseaux neuronaux (TensorFlow/Keras)** : Pour des prédictions plus sophistiquées si le dataset est volumineux.
- Évalue les performances des modèles (R², MAE, RMSE).

---

#### 5. **Visualisation des résultats :**
- Présente les résultats du modèle avec des graphiques :
  - Graphiques de comparaison entre les valeurs prédites et les valeurs réelles.
  - Importance des features dans le modèle (via SHAP ou des barplots).
  - Tableau interactif (via **Dash** ou **Streamlit**) permettant de visualiser les performances des joueurs.

---

#### 6. **Approfondissements :**
- Ajoute des prédictions pour les équipes (victoires/défaites, scores totaux).
- Crée des scénarios "what-if" (par exemple : impact d'une blessure ou d'un changement de minutes jouées).

---

### **Compétences mobilisées :**
- **Machine learning** : Régression, arbres de décision, réseaux neuronaux.
- **Data visualisation** : Matplotlib, Seaborn, Plotly, Dash/Streamlit.
- **Data engineering** : Collecte de données, nettoyage, feature engineering.
- **Outils** : Python, Pandas, NumPy, Scikit-learn, TensorFlow/Keras.

---

Tu peux publier ton projet sur GitHub avec un notebook clair pour démontrer tes compétences. Si tu veux des détails sur un des points (comme les APIs ou le code), dis-le-moi !