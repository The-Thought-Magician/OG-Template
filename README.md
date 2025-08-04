# OG-Template

## Introduction

A fucking cool template that has backend set up with fastapi, allows you to build anything with it, has integration of n8n -> codebase. Bruhhhh, very frustrated i cant find shit on good templates. Building for the community man. 


## Current Features

*   **FastAPI Foundation:** Modern, fast web framework for building APIs with Python 3.11+
*   **Modular Architecture:** Clean directory structure with organized modules
*   **Docker Support:** Containerized application with Docker and Docker Compose
*   **UV Package Manager:** Fast Python package installer and resolver
*   **Testing Setup:** Pre-configured testing environment with pytest
*   **Development Scripts:** Helper scripts for running and managing the application
*   **Configuration Management:** Environment-based configuration with .env support
*   **API Documentation:** Auto-generated OpenAPI/Swagger documentation
*   **Middleware Support:** CORS and logging middleware included
*   **User Management:** Basic user CRUD operations with in-memory storage
*   **Structured Validation:** Pydantic-like schema validation
*   **Service Layer:** Business logic separated into service classes
*   **Controller Pattern:** Request handling with controller classes

## Planned Features (In Development)

*   **Provider Integration:** Modules for popular cloud services (AWS, GCP, Azure)
*   **Database Support:** Multiple database support (PostgreSQL, MySQL, MongoDB)
*   **Authentication:** JWT, OAuth2, and API key authentication strategies
*   **n8n Workflow Converter:** Convert n8n JSON workflows into backend code

## Getting Started

### Prerequisites

*   **Python 3.11+:** Required for FastAPI and modern Python features
*   **UV Package Manager:** For fast dependency management (installed automatically in Docker)
*   **Docker & Docker Compose:** For containerized development (optional but recommended)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/The-Thought-Magician/OG-Template.git
    cd OG-Template
    ```

2.  **Using Docker (Recommended):**
    ```bash
    docker-compose up --build
    ```
    The application will be available at `http://localhost:8000`

3.  **Local Development:**
    ```bash
    # Install UV if not already installed
    pip install uv
    
    # Install dependencies
    uv pip install fastapi uvicorn
    
    # Run the application
    uvicorn app.main:app --reload
    ```
    The application will be available at `http://localhost:8000`

4.  **Using the run script:**
    ```bash
    chmod +x scripts/run.sh
    ./scripts/run.sh
    ```

5.  **Quick setup with setup script:**
    ```bash
    chmod +x setup.sh
    ./setup.sh
    ```

### Testing

Run the test suite:
```bash
# Install test dependencies
uv pip install pytest httpx

# Run tests
pytest tests/
```

### API Testing

Test the API endpoints:
```bash
# Make sure the server is running, then:
chmod +x scripts/test_api.sh
./scripts/test_api.sh
```

### Usage

The template includes a comprehensive FastAPI application with:
- RESTful API endpoints with proper HTTP methods
- User management system with CRUD operations
- Health check and monitoring endpoints
- Modular architecture with services, controllers, and models
- Environment-based configuration
- Automatic API documentation
- Request/response validation
- Error handling and logging

## Directory Structure

```
OG-Template/
├── app/                          # Main application code
│   ├── main.py                   # FastAPI application entry point
│   ├── config/                   # Configuration files
│   ├── controllers/              # Request handlers and business logic
│   ├── db/                       # Database related code
│   │   ├── migrations/           # Database migrations
│   │   └── seeders/              # Database seeders
│   ├── interfaces/               # Interface definitions and contracts
│   ├── middleware/               # Custom middleware
│   ├── models/                   # Data models
│   ├── n8n_converter/           # n8n workflow conversion tools
│   │   ├── parser/              # JSON workflow parsers
│   │   └── templates/           # Code generation templates
│   ├── routes/                  # API route definitions
│   ├── schema/                  # Pydantic schemas and validation
│   ├── services/                # Business logic services
│   │   ├── auth/                # Authentication services
│   │   └── core/                # Core business services
│   ├── utils/                   # Utility functions
│   ├── validators/              # Custom validators
│   └── workflows/               # Workflow definitions
├── docs/                        # Documentation
├── scripts/                     # Development and deployment scripts
│   └── run.sh                   # Application runner script
├── tests/                       # Test files
│   └── test_main.py            # Main application tests
├── docker-compose.yaml         # Docker Compose configuration
├── dockercompose.yaml          # Alternative Docker Compose config
├── Dockerfile                  # Docker image definition
├── pyproject.toml             # Python project configuration
├── setup.sh                   # Setup script (placeholder)
├── ideas.md                   # Development ideas and roadmap
├── LICENSE                    # MIT License
└── README.md                  # This file
```

## Current API Endpoints

### Core Endpoints
- **GET /**: Returns welcome message and app information
- **GET /health**: Health check endpoint
- **GET /docs**: Auto-generated API documentation (Swagger UI)
- **GET /redoc**: Alternative API documentation (ReDoc)

### API v1 Endpoints
- **GET /api/v1/health/**: API health check
- **GET /api/v1/health/ping**: Simple ping endpoint
- **GET /api/v1/info**: Application information
- **POST /api/v1/users/**: Create a new user
- **GET /api/v1/users/**: Get all users
- **GET /api/v1/users/{user_id}**: Get user by ID
- **PUT /api/v1/users/{user_id}**: Update user
- **DELETE /api/v1/users/{user_id}**: Delete user

## Technology Stack

- **Backend Framework:** FastAPI
- **Python Version:** 3.11+
- **Package Manager:** UV
- **Containerization:** Docker & Docker Compose
- **Testing:** pytest
- **ASGI Server:** Uvicorn

## Development Roadmap

See `ideas.md` for a comprehensive list of planned features and enhancements.

### Next Steps
1. Implement core authentication system
2. Add database integration with ORM support
3. Create provider abstraction layer for cloud services
4. Develop n8n workflow converter functionality
5. Add comprehensive logging and monitoring
6. Create CLI tool for scaffolding

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the [MIT License](LICENSE).