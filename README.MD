
#Legends of Costa Rica - Backend

Backend developed using **FastAPI** to manage popular Costa Rican legends. It supports CRUD operations, location and category filtering, JWT authentication, and image uploads with Cloudinary.

---

##  Technologies used

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [Cloudinary](https://cloudinary.com/)
- [JWT Auth](https://jwt.io/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Uvicorn](https://www.uvicorn.org/)


## DB installation
Mysql must be installed and the 4thewords_db_kerly_sarrias.sql must be imported

## installation

1. Clone the repository

```bash
git clone https://github.com/KerlyVanesaSarrias/KerlyVanesaSarrias-4thewords_backend_kerly_sarrias
cd 4thewords_backend
```

2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```
```bash
cd 4thewords_backend
python -m venv venv
.\venv\Scripts\Activate.ps1 
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8080


---

## ⚙️ Environment variables

Create a `.env` file in the project root with the following variables:

```send



APP_NAME=4thewords_backend
DATABASE_URL=postgresql://user:password@localhost:5432/legends_db
JWT_SECRET_KEY=your_secret_key
CLOUDINARY_CLOUD_NAME=your_cloudinary_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
JWT_ALGORITHM=HS256
JWT_EXPIRATION_MINUTES=60
```

---

## 🛠 Migrations with Alembic

```bash
alembic revision --autogenerate -m "initial"
alembic upgrade head
```

---

## ▶️ Run the server

```bash
uvicorn app.main:app --reload
```

Access [http://localhost:8000](http://localhost:8000)

---

## 📬 Main Endpoints

| Method | Path | Description |
|--------|--------------------|-----------------------------------|
| GET | `/legends/` | List legends (with filters) |
| POST | `/legends/` | Create a new legend |
| GET | `/legends/{id}` | Get a specific legend |
| PUT | `/legends/{id}` | Update an existing legend |
| DELETE | `/legends/{id}` | Delete a legend |
| GET | `/categories/` | List categories |
| POST | `/categories/` | Create a new category |
| GET | `/locations/provinces/` | List provinces |
| GET | `/locations/provinces/{id}/cantons` | List cantons by province |
| GET | `/locations/canton/{id}/districts` | List districts by canton |
| POST | `/locations/provinces/` | create provinces |
| POST | `/locations/cantons/` | create cantons |
| POST | `/locations/districts/` | create districts |

| POST | `/auth/login` | Log in (returns JWT) |
| POST | `/auth/register` | Register (returns JWT) |
| POST | `/auth/me` | get profile |

---

## 🖼 Image Upload

Images are automatically uploaded to **Cloudinary** using `cloudinary.uploader.upload()`.

---

## 🔐 Authentication

The backend protects routes using JWT. To access protected routes:

```http
Authorization: Bearer <token>
```

---

##  Author

Developed by **Kerly Vanessa Sarrias*