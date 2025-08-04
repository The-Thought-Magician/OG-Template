#!/bin/bash

echo "🔧 Setting up OG-Template..."

# Create .env file from example if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file from .env.example..."
    cp .env.example .env
    echo "✅ Created .env file. Please update it with your configuration."
fi

# Install UV if not available
if ! command -v uv &> /dev/null; then
    echo "Installing UV package manager..."
    pip install uv
fi

# Install dependencies
echo "Installing dependencies..."
uv pip install -r requirements.txt

# Install development dependencies
echo "Installing development dependencies..."
uv pip install pytest httpx black isort flake8

# Make scripts executable
echo "Making scripts executable..."
chmod +x scripts/run.sh

echo "🎉 Setup complete! You can now run:"
echo "  ./scripts/run.sh    # Start development server"
echo "  pytest tests/       # Run tests"
echo "  docker-compose up   # Run with Docker"