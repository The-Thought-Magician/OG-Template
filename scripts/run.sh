#!/bin/bash

uv pip install -r requirements.txt
uvicorn app.main:app --reload
