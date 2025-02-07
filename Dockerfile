# Utiliser Python 3.12 sur Alpine
FROM python:3.12.9-alpine

# Installer les paquets nécessaires (important pour Alpine)
RUN apk add --no-cache gcc musl-dev libffi-dev

# Définir le dossier de travail
WORKDIR /app

# Copier uniquement requirements.txt pour optimiser le cache Docker
COPY requirements.txt /app/

# Installer les dépendances AVANT de copier le reste du pro