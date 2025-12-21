# SmartShop AI - Backend

AI-powered shopping assistant backend built with FastAPI and Python.

## 🏗️ Architecture Overview

This backend follows a clean, layered architecture with:

- **Repository Pattern** for data access abstraction
- **Service Layer** for business logic
- **Dependency Injection** for loose coupling
- **Middleware Stack** for cross-cutting concerns
- **ML Components** for AI functionality

### Project Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── core/                # Core configurations (config, database, logging)
│   ├── api/v1/              # API routes (search, compare, recommendations)
│   ├── schemas/             # Pydantic models for validation
│   ├── models/              # Database models
│   ├── repositories/        # Repository pattern implementation
│   ├── services/            # Business logic layer
│   ├── ml/                  # ML components (NLP, embeddings, ranking)
│   ├── data_sources/        # Data source abstractions
│   ├── cache/               # Caching layer (Redis)
│   ├── middlewares/         # Custom middlewares
│   └── utils/               # Utility functions
├── tests/                   # Test suite
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variables template
├── Dockerfile               # Docker configuration
└── README.md                # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Redis (optional, for caching)
- Virtual environment tool (venv, conda, etc.)

### Installation

1. **Clone the repository**
   ```bash
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run the development server**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

6. **Access the API**
   - API Documentation: http://localhost:8000/docs
   - Alternative Docs: http://localhost:8000/redoc
   - Health Check: http://localhost:8000/api/v1/health

## 📚 API Endpoints

### Search
- `POST /api/v1/search` - Natural language product search

### Comparison
- `POST /api/v1/compare` - Compare multiple products

### Recommendations
- `GET /api/v1/products/{product_id}/recommendations` - Get product recommendations

### Health
- `GET /api/v1/health` - Health check endpoint

## 🧪 Testing

Run tests with pytest:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run specific test file
pytest tests/test_search.py -v
```

## 🔧 Development

### Code Quality

```bash
# Format code with black
black app/

# Lint with flake8
flake8 app/

# Type checking with mypy
mypy app/
```

### Project Conventions

- Use **async/await** for I/O operations
- Follow **PEP 8** style guide
- Add **type hints** to all functions
- Write **docstrings** for public methods
- Keep functions **focused** and **single-purpose**

## 🏛️ Architecture Patterns

### Repository Pattern
All database access goes through repositories, allowing easy mocking and testing.

### Service Layer
Business logic is encapsulated in services, keeping controllers thin.

### Dependency Injection
FastAPI's dependency injection system is used throughout for better testability.

### Middleware
Cross-cutting concerns (logging, rate limiting, error handling) are handled by middleware.

## 📝 Configuration

Configuration is managed through environment variables using Pydantic Settings.
See `.env.example` for all available options.

## 🐳 Docker

Build and run with Docker:

```bash
docker build -t smartshop-backend .
docker run -p 8000:8000 smartshop-backend
```

## 📄 License

This project is part of the SmartShop AI portfolio project.

## 🤝 Contributing

This is a portfolio project. While not open for contributions, feedback is welcome!
