# AI Turf Receptionist

> **Enterprise-grade AI-powered sports turf booking and management SaaS
> built with FastAPI, React, PostgreSQL, and Docker.** This project
> demonstrates the complete Software Development Life Cycle (SDLC), from
> business analysis and architecture to implementation, testing,
> deployment, and operations.

------------------------------------------------------------------------

# Project Overview

AI Turf Receptionist is a SaaS platform designed to automate sports turf
bookings and simplify turf management.

## Features

### Customer

-   Automated IVR-based booking
-   Check slot availability
-   Advance payment
-   SMS/WhatsApp confirmation

### Turf Owner

-   Dashboard
-   Turf management
-   Slot management
-   Booking management
-   Payment tracking

### Administrator

-   Owner management
-   Audit logs
-   Platform monitoring

------------------------------------------------------------------------

# Technology Stack

## Backend

-   Python
-   FastAPI
-   SQLAlchemy
-   Alembic
-   JWT

## Frontend

-   React
-   TypeScript

## Database

-   PostgreSQL

## DevOps

-   Docker
-   Nginx
-   GitHub Actions (Planned)

------------------------------------------------------------------------

# Project Structure

``` text
ai-turf-receptionist/
├── backend/
├── frontend/
├── database/
├── deployment/
├── docs/
├── diagrams/
└── README.md
```

------------------------------------------------------------------------

# Development Roadmap

-   [x] Documentation
-   [ ] Backend
-   [ ] Frontend
-   [ ] IVR Integration
-   [ ] Payment Integration
-   [ ] Deployment
-   [ ] AI Voice Assistant

------------------------------------------------------------------------

# Installation

``` bash
git clone https://github.com/<your-username>/ai-turf-receptionist.git
cd ai-turf-receptionist
```

## Backend

``` bash
cd backend
python -m venv venv
pip install -r requirements.txt
uvicorn app.main:app --reload
```

------------------------------------------------------------------------

# API Documentation

-   Swagger: http://localhost:8000/docs
-   ReDoc: http://localhost:8000/redoc

------------------------------------------------------------------------

# License



------------------------------------------------------------------------

# Author

**Vishnu Harikumar**
