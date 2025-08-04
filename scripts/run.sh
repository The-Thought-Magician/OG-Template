#!/bin/bash

echo "🚀 Starting OG-Template development server..."

# Check if virtual environment exists, create if not
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install UV if not available
if ! command -v uv &> /dev/null; then
    echo "Installing UV package manager..."
    pip install uv
fi

# Install dependencies
echo "Installing dependencies..."
uv pip install -r requirements.txt

# Run the application
echo "Starting FastAPI server..."
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
