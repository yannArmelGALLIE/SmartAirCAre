# 🩺 SmartAirCare

**Système Hybride Intelligent de Prévention des Maladies Respiratoires**

---

## 📌 Description

SmartAirCare est une solution **HealthTech innovante** combinant **IoT, Intelligence Artificielle et réseau hybride (LoRa + Internet)** pour détecter précocement les maladies respiratoires, notamment la pneumonie.

Le système garantit une **connectivité continue**, même en zones à faible réseau, tout en assurant la **confidentialité des données médicales** grâce à une cryptographie distribuée.

---

## 🚀 Objectifs

- Détecter précocement les anomalies respiratoires
- Assurer un suivi continu des patients
- Envoyer automatiquement les alertes aux cliniques
- Fonctionner même sans connexion Internet stable
- Protéger les données médicales des utilisateurs

---

## 🧠 Fonctionnalités principales

### 🔁 IA de Routage Hybride
- Choix automatique entre **LoRa** et **Internet**
- Basé sur :
  - Qualité du réseau
  - Criticité des données
  - Niveau de batterie
  - Latence requise

---

### ☁️ Backend Double (Edge + Cloud)
- **Cloud** : stockage global, analytics, dashboard
- **Local (Edge)** :
  - Fonctionne sans Internet
  - Continue les analyses IA
  - Synchronisation automatique au retour du réseau

---

### 🔐 Cryptographie Distribuée
- Données chiffrées (AES-256, TLS 1.3)
- Clé privée unique par utilisateur
- Inspiré du modèle blockchain
- Accès aux données uniquement avec consentement

---

### 🏥 Intégration des Cliniques
- Détection automatique d’anomalies
- Envoi des données à la clinique la plus proche
- Alertes multi-canaux :
  - SMS
  - Email
  - Notification mobile

---

## 📡 Architecture du système

### 🔹 AirHome (Station principale)
- Raspberry Pi
- Capteurs environnementaux
- Backend local

### 🔹 AirBand (Bracelet intelligent)
- SpO₂
- Fréquence cardiaque
- Température corporelle
- Communication LoRa

---

## 🤖 Modules IA

| Module | Rôle |
|------|------|
| IA de routage | Décide du canal de communication |
| IA de toux | Analyse audio pour détecter anomalies |
| IA capteurs | Calcule un score de risque |

### 🎯 Score de risque global
- IA Toux : 40%
- Physiologique : 30%
- Environnemental : 20%
- Questionnaire : 10%

---

## 🛠️ Technologies utilisées

### Hardware
- ESP32
- Raspberry Pi
- Capteurs (DHT22, MQ-135, MAX30102, DS18B20)
- Modules LoRa (SX1276)

### Software
- Python
- Django / FastAPI
- React Native
- SQLite / PostgreSQL

### IA
- CNN (analyse de la toux)
- TensorFlow Lite
- Modèles de régression et classification

### Réseau & Sécurité
- LoRa
- MQTT
- TLS 1.3
- AES-256
- Ed25519

---

## 📊 État du projet

✅ Prototype fonctionnel  
✅ Communication LoRa validée (1.2 km)  
✅ Backend local opérationnel  
✅ IA toux (Accuracy 87.3%)  
🔄 Cryptographie en cours  
🔄 Intégration clinique en négociation  

---

## 💰 Modèle économique

| Source | Cible |
|------|------|
| Vente kit | Familles, écoles |
| SaaS | Cliniques |
| Licence | États / hôpitaux |
| API data | Chercheurs |

---

## 📈 Roadmap

### Année 1
- Déploiement à Abidjan
- 50 kits
- 3 cliniques partenaires

### Année 2
- Extension nationale
- 300 kits

### Année 3
- Expansion CEDEAO

---

## 👥 Équipe

### 👨‍💻 GALLIE Koffi Yann-Armel
- Chef d'équipe
- IoT & IA
- Routage hybride & analyse de la toux

### 🔐 NABE Nana Hilaire
- Réseaux & Sécurité
- IA capteurs & cryptographie

### 📱 TOKAPIEU Ezechiel
- Développement logiciel
- App mobile & backend

---


## 🌍 Zone cible

- 🇨🇮 Côte d’Ivoire (pilote : Abidjan)
- 🌍 Extension CEDEAO

---

## 📜 Licence

Projet académique / prototype – droits réservés à l’équipe SmartAirCare.

---

## 📬 Contact

Pour toute collaboration ou partenariat :
- Email : professional.gallie@gmail.com *(à adapter)*

---

## ⚠️ Disclaimer

SmartAirCare est un outil d’assistance médicale et ne remplace pas un diagnostic professionnel.

---