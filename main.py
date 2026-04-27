import os
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

print("\n📊 Génération des données...")
np.random.seed(42)
n = 2000

data = pd.DataFrame({
    'heart_rate':     np.random.normal(75, 12, n),
    'spo2':           np.random.uniform(92, 100, n),
    'skin_temp':      np.random.normal(36.5, 0.8, n),
    'rr_variability': np.random.normal(50, 15, n),
    'co2_ppm':        np.random.normal(700, 300, n),
    'ambient_temp':   np.random.normal(22, 5, n),
    'humidity':       np.random.uniform(30, 80, n),
    'voc_ppb':        np.random.normal(200, 100, n),
    'pm25':           np.random.normal(15, 10, n),
    'noise_db':       np.random.normal(45, 15, n),
    'lux':            np.random.normal(300, 150, n),
})

def label_environment(row):
    score = 0
    if row['co2_ppm'] > 1000:  score += 2
    if row['co2_ppm'] > 1500:  score += 2
    if row['pm25'] > 25:        score += 2
    if row['voc_ppb'] > 400:    score += 1
    if row['heart_rate'] > 100: score += 1
    if row['spo2'] < 95:        score += 2
    if row['noise_db'] > 70:    score += 1
    if row['humidity'] > 70 or row['humidity'] < 30: score += 1
    if score >= 5: return 2
    elif score >= 2: return 1
    else: return 0

data['label'] = data.apply(label_environment, axis=1)
os.makedirs('data', exist_ok=True)
data.to_csv('data/dataset.csv', index=False)
print("✅ Dataset généré")

FEATURES = ['heart_rate','spo2','skin_temp','rr_variability',
            'co2_ppm','ambient_temp','humidity','voc_ppb','pm25','noise_db','lux']

X = data[FEATURES]
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled  = scaler.transform(X_test)

print("\n🤖 Entraînement du modèle...")
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    min_samples_split=5,
    random_state=42,
    class_weight='balanced'
)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)
print(classification_report(y_test, y_pred,
      target_names=['Sain', 'Modéré', 'Dangereux']))

os.makedirs('models', exist_ok=True)
joblib.dump(model,  'models/model_rf.pkl')
joblib.dump(scaler, 'models/scaler.pkl')
print("✅ Modèle sauvegardé")
