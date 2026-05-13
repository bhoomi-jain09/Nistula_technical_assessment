# Nistula Technical Assessment

This repository contains a production-style backend implementation designed as part of the Nistula technical assessment.
The solution demonstrates **API design, database structuring, and logic-driven confidence scoring**, focusing on scalability, maintainability, and real-world engineering thinking.


#  System Overview

The system is divided into three core components:

* **Part 1: Webhook/API Layer**

  * Handles incoming requests
  * Validates and processes payloads
  * Designed with modular service separation

* **Part 2: Database Schema Design**

  * Structured relational schema
  * Optimized for scalability and data integrity
  * Includes proper indexing strategy considerations

* **Part 3: System Design & Thinking**

  * Explains architectural decisions
  * Covers trade-offs, scalability, and reliability considerations

# Project Structure
nistula-technical-assessment/
│
├── app/ or src/          # API / Webhook implementation
├── schema.sql            # Database schema (Part 2)
├── thinking.md           # System design reasoning (Part 3)
├── README.md             # Documentation + setup guide
├── .env.example          # Environment variable template

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/bhoomi-jain09/Nistula_technical_assessment.git
cd Nistula_technical_assessment

## 2. Create Virtual Environment

```bash
python -m venv venv
Activate environment:

**Windows**

```bash
venv\Scripts\activate

## 3. Install Dependencies

```bash
pip install -r requirements.txt

## 4. Environment Configuration
Create a `.env` file using `.env.example`:

```env
API_KEY=
DATABASE_URL=

> Note: No sensitive keys are committed to the repository. Only templates are shared for security.

## 5. Run Application

```bash
uvicorn app.main:app --reload

# API Design

### POST `/webhook`
* Accepts incoming event payloads
* Performs validation and normalization
* Routes data into processing pipeline

# Confidence Scoring Logic (Core Intelligence Layer)

One of the key components of this system is a **rule-based confidence scoring engine** that evaluates the reliability of extracted or inferred outputs.
The goal is to simulate a lightweight decision intelligence layer that can later be extended into ML-based scoring

## Design Philosophy
Instead of relying on a single metric, the system uses a **multi-factor weighted model** to ensure balanced decision-making:
* Avoids over-dependence on keywords
* Balances semantic + contextual understanding
* Ensures predictable and explainable outputs
* 
## Scoring Factors

### 1. Intent Alignment (40%)
Measures how accurately the input matches expected system intent patterns.

### 2. Keyword Relevance (30%)
Evaluates direct overlap between input tokens and known domain keywords.

### 3. Contextual Similarity (30%)
Assesses semantic consistency with historical or contextual patterns.

## Final Scoring Formula

Confidence Score =
(0.4 × Intent Alignment) +
(0.3 × Keyword Relevance) +
(0.3 × Contextual Similarity

## Score Interpretation

* **0.75 – 1.0 → High Confidence**
  → System can auto-accept response

* **0.50 – 0.75 → Medium Confidence**
  → Requires validation or fallback logic

* **Below 0.50 → Low Confidence**
  → Escalation or rejection triggered
  
## Engineering Insight
This scoring model is intentionally designed to be:

* **Explainable** (no black-box dependency)
* **Modular** (weights can be tuned dynamically)
* **Extensible** (can be replaced with ML/NLP model later)

# Assumptions
* PostgreSQL is used as the database layer
* Webhook payloads are JSON structured
* System is designed for extensibility, not just functionality
* Confidence logic is heuristic but ML-ready

# Future Improvements

* Replace heuristic scoring with ML-based classifier
* Introduce event queue (Kafka / Celery)
* Add authentication & rate limiting
* Implement logging + observability layer
* Containerize using Docker for deployment consistency

