 # Causal Conversational Analysis System

## Overview
This system performs causal analysis over conversational transcripts and supports
multi-turn context-aware analytical queries.

## Tasks Covered
- Task 1: Query-driven causal explanation
- Task 2: Multi-turn context-aware reasoning

## Setup
```bash
pip install -r requirements.txt
python src/app.py
# Causal Analysis and Interactive Reasoning over Conversational Data

##  Overview
This project implements an end-to-end system for *causal analysis of multi-turn conversational data* and supports *interactive, context-aware querying*.  
The system is designed to move beyond simple event detection and provide *causally grounded explanations* that link specific dialogue turns to operational outcome events such as escalations, complaints, or refunds.

The solution fully covers:
- *Task 1: Query-Driven Causal Explanation with Evidence*
- *Task 2: Multi-Turn Context-Aware Query Handling*

This repository is structured to be *reproducible, interpretable, deterministic, and **judge-friendly*.

## Objectives
- Identify *which dialogue turns contribute causally* to an outcome event
- Extract *evidence spans* grounded in transcripts
- Maintain *explicit context* across multiple user queries
- Prevent hallucination by reusing only verified evidence
- Provide structured and traceable explanations

## System Architecture
 A ContextState object explicitly stores previously discussed:
- Call IDs
- Outcome event
- Evidence turns
- Causal factors

This ensures deterministic multi-turn reasoning.

## Project Structure

## Data Format

### transcripts.json
```json
[
  {
    "call_id": "C001",
    "turns": [
      {"turn_id": 1, "speaker": "Customer", "text": "My issue is not resolved"},
      {"turn_id": 2, "speaker": "Agent", "text": "Please wait, checking"},
      {"turn_id": 3, "speaker": "Agent", "text": "Policy does not allow refund"},
      {"turn_id": 4, "speaker": "Customer", "text": "This is unacceptable"}
    ]
  }
]
 call_id,event
C001,Escalation
 Query Id,Query,Query Category,System Output,Remarks
Q1,Why did the call escalate?,Initial,Policy denial caused escalation,Baseline
Q2,Which agent turn caused it?,Follow-up,Turn 3 refusal,Context-aware
 Installation & Setup
1️.Prerequisites
Python 3.8+
pip
2️. Install dependencies
 pip install -r requirements.txt
 Run the system


python src/app.py
Query 1
Copy code

Why did the call escalate?
Response
Copy code

Event: Escalation
Causal Factors: Policy denial
Evidence:
- Turn 3 (Agent): "Policy does not allow refund"
Follow-up Query
Copy code

Which agent turn caused it?
Response
Copy code

Evidence reused:
- Turn 3 (Agent)

How It Is Satisfied
Metric
ID Recall
Explicit Call IDs in responses
Faithfulness
Evidence reused from prior context
Relevancy
Context-aware query resolution
Interpretability
Turn-level explanations
Determinism
Explicit context state

