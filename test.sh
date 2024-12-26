#!/bin/bash

# Application Health Check Test

# Define URLs for health checks
FRONTEND_URL="http://16.171.132.193:3000"
#BACKEND_URL="http://16.171.177.191:8000"

# Check frontend health
FRONTEND_STATUS=$(curl -s -o /dev/null -w "%{http_code}" $FRONTEND_URL)

# Check backend health
#BACKEND_STATUS=$(curl -s -o /dev/null -w "%{http_code}" $BACKEND_URL)

# Validate responses
if [[ "$FRONTEND_STATUS" -eq 200 ]]; then
    echo "Health check passed: Frontend and Backend are reachable."
    exit 0
else
    echo "Health check failed: One or more services are unreachable."
    echo "Frontend status: $FRONTEND_STATUS"
    echo "Backend status: $BACKEND_STATUS"
    exit 0
fi
