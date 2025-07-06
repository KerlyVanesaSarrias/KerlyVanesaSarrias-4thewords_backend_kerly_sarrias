# 4thewords Backend

Este es el backend del proyecto **4thewords**, desarrollado con **FastAPI**, **SQLModel**, **MySQL** y **Uvicorn**.

## 🚀 Tecnologías usadas

- Python 3.11+
- FastAPI
- SQLModel
- MySQL
- Uvicorn
- Pydantic Settings
- Email Validator

---

## Intalacion BD
Se debe instalar mysql e importar el schema.sql

## 📦 Instalación

```bash
cd 4thewords_backend
python -m venv venv
.\venv\Scripts\Activate.ps1 
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8080