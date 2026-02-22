Diamond Price Prediction using KNN & Streamlit
📌 Project Overview

This project builds an end-to-end Machine Learning application to predict diamond prices using the K-Nearest Neighbors (KNN) Regressor.

The model is trained using proper preprocessing techniques and deployed using Streamlit Cloud.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🚀 Live Demo
🔗 Streamlit Deployment Link:
--> https://diamondpricepredction-uh92ylyrifhzwt6vdkp4cx.streamlit.app/

📂 Project Structure
Diamond-Price-Prediction/
- │
- ├── app.py                     # Streamlit application
- ├── train_model.py             # Model training script
- ├── diamond_knn_model.pkl      # Saved trained pipeline
- ├── diamonds.csv               # Dataset
- ├── requirements.txt           # Required packages
- └── README.md

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📊 Dataset Information
Features used:
- Numerical Features: carat, depth, table, x, y, z
- Categorical Features: cut, color, clarity
- Target Variable: price

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🛠️ Machine Learning Pipeline
🔹 Data Preprocessing
- 75:25 Train-Test split
- Removed invalid values (x, y, z = 0)
- Handled outliers
- Log transformation applied to price
- OneHotEncoding for categorical features
- Standard Scaling for numerical features

🔹 Model
- K-Nearest Neighbors Regressor
- Hyperparameter tuning using GridSearchCV
- Parameters tuned:
- n_neighbors
- weights (uniform, distance)
- p (Minkowski distance metric)


🔹 Evaluation Metrics
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

- Model Performance:
- R² Score ≈ 0.98+

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🖥️ Streamlit Application
The app:
- Takes user input for diamond features
- Loads the saved pipeline
- Predicts price
- Converts log prediction back to original scale
- Displays final predicted price

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📦 Installation (For Local Run)
- git clone <your-repo-link>
- cd Diamond-Price-Prediction
- pip install -r requirements.txt
- streamlit run app.py

☁️ Deployment

- This application is deployed using Streamlit Cloud.
- Steps followed:
- 1.Pushed project to GitHub
- 2.Connected repository to Streamlit Cloud
- 3.Deployed app.py
- 4.Generated public link
