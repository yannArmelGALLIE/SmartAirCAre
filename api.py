from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib
import json
import os
from datetime import datetime

model  = joblib.load('models/model_rf.pkl')
scaler = joblib.load('models/scaler.pkl')

FEATURES = ['heart_rate','spo2','skin_temp','rr_variability',
            'co2_ppm','ambient_temp','humidity','voc_ppb','pm25','noise_db','lux']
LABELS   = {0: 'Sain', 1: 'Modéré', 2: 'Dangereux'}
CONSEILS = {
    0: "Environnement sain. Aucune action requise.",
    1: "Légère dégradation. Aérez la pièce.",
    2: "ALERTE : Quittez ou activez la ventilation !"
}
HISTORIQUE_FILE = 'historique.json'

app = FastAPI(
    title="IA Environnement & Santé",
    description="API d'analyse des données physiologiques et environnementales",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class DonneesEnvironnement(BaseModel):
    heart_rate:     float
    spo2:           float
    skin_temp:      float
    rr_variability: float
    co2_ppm:        float
    ambient_temp:   float
    humidity:       float
    voc_ppb:        float
    pm25:           float
    noise_db:       float
    lux:            float

def charger_historique():
    if os.path.exists(HISTORIQUE_FILE):
        with open(HISTORIQUE_FILE, 'r') as f:
            return json.load(f)
    return []

def sauvegarder_historique(entry):
    historique = charger_historique()
    historique.append(entry)
    with open(HISTORIQUE_FILE, 'w') as f:
        json.dump(historique, f, indent=2)

@app.get("/")
def accueil():
    return {
        "message": "✅ API IA Environnement opérationnelle",
        "version": "1.0.0",
        "routes": ["/analyser", "/historique", "/sante"]
    }

@app.post("/analyser")
def analyser(donnees: DonneesEnvironnement):
    try:
        df     = pd.DataFrame([donnees.model_dump()])[FEATURES]
        scaled = scaler.transform(df)
        pred   = model.predict(scaled)[0]
        proba  = model.predict_proba(scaled)[0]
        resultat = {
            "timestamp":   datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "statut":      LABELS[int(pred)],
            "confiance":   f"{max(proba)*100:.1f}%",
            "conseil":     CONSEILS[int(pred)],
            "probabilites": {
                "Sain":      f"{proba[0]*100:.1f}%",
                "Modéré":    f"{proba[1]*100:.1f}%",
                "Dangereux": f"{proba[2]*100:.1f}%"
            },
            "donnees_recues": donnees.model_dump()
        }
        sauvegarder_historique(resultat)
        return resultat
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/historique")
def historique(limit: int = 10):
    historique = charger_historique()
    return {
        "total":     len(historique),
        "resultats": historique[-limit:]
    }

@app.get("/sante")
def sante_globale():
    historique = charger_historique()
    if not historique:
        return {"message": "Aucune analyse effectuée pour le moment."}
    total     = len(historique)
    sains     = sum(1 for h in historique if h['statut'] == 'Sain')
    moderes   = sum(1 for h in historique if h['statut'] == 'Modéré')
    dangereux = sum(1 for h in historique if h['statut'] == 'Dangereux')
    return {
        "total_analyses": total,
        "repartition": {
            "Sain":      f"{sains} ({sains/total*100:.1f}%)",
            "Modéré":    f"{moderes} ({moderes/total*100:.1f}%)",
            "Dangereux": f"{dangereux} ({dangereux/total*100:.1f}%)"
        },
        "derniere_analyse": historique[-1]['timestamp']
    }
