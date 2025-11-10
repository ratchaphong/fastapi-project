# FastAPI Project

FastAPI project ที่ใช้ Poetry สำหรับจัดการ dependencies

## ความต้องการของระบบ

- Python 3.14+
- Poetry

## การติดตั้ง Poetry

### macOS / Linux

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Windows

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

### ตรวจสอบการติดตั้ง

```bash
poetry --version
```

## การตั้งค่าโปรเจกต์

### 1. ติดตั้ง dependencies ด้วย Poetry

```bash
poetry install
```

### 2. ตั้งค่า Environment Variables

คัดลอกไฟล์ `env.example` เป็น `.env`:

```bash
cp env.example .env
```

แก้ไขค่าตามต้องการในไฟล์ `.env`

## การรันแอปพลิเคชัน

### รันด้วย Poetry

```bash
poetry run uvicorn main:app --reload
```

แอปพลิเคชันจะรันที่: `http://localhost:8000`

### รันด้วย Docker Compose

```bash
docker-compose up -d
```

## การจัดการ Dependencies ด้วย Poetry

### เพิ่ม dependency

```bash
poetry add package-name
```

### ลบ dependency

```bash
poetry remove package-name
```

### อัปเดต dependencies

```bash
poetry update
```

### ดู dependencies

```bash
poetry show
```

## API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
