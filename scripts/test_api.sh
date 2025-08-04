#!/bin/bash

echo "🧪 Testing OG-Template API endpoints..."

# Base URL
BASE_URL="http://localhost:8000"

echo "1. Testing root endpoint..."
curl -s "$BASE_URL/" | python3 -m json.tool

echo -e "\n2. Testing health check..."
curl -s "$BASE_URL/health" | python3 -m json.tool

echo -e "\n3. Testing API health..."
curl -s "$BASE_URL/api/v1/health/" | python3 -m json.tool

echo -e "\n4. Testing app info..."
curl -s "$BASE_URL/api/v1/info" | python3 -m json.tool

echo -e "\n5. Creating a test user..."
curl -s -X POST "$BASE_URL/api/v1/users/" \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "email": "test@example.com", "full_name": "Test User"}' | python3 -m json.tool

echo -e "\n6. Getting all users..."
curl -s "$BASE_URL/api/v1/users/" | python3 -m json.tool

echo -e "\n7. Getting user by ID..."
curl -s "$BASE_URL/api/v1/users/1" | python3 -m json.tool

echo -e "\n✅ API testing complete!"
