# Cogniton Protocol Specification (CP-v0.1)

## 1. Introduction

This protocol defines the structure, encoding, and lifecycle of a Cogniton (Ω) particle within the Cogniton Collider array. It establishes the initial data layer for the future **CogniChain** architecture.

## 2. Cogniton Data Structure (C-Struct)

Every raw Cogniton emitted by a user must adhere to the following minimal structure:

| Field | Type | Description |
|---|---|---|
| `cogniton_id` | STRING (UUID) | Unique identifier for the raw Cogniton. |
| `timestamp` | DATETIME | The moment of emission (critical for 9.4s decay). |
| `source_id` | STRING | Hashed, anonymized user ID (for CogniProof credit). |
| `content_hash` | STRING | SHA-256 hash of the input text/voice (ensures immutability). |
| `vector_embedding` | ARRAY (FLOAT) | High-dimensional vector representation (e.g., 768 or 1536 dim). |
| `negative_entropy` | FLOAT | Calculated -ΔS value (energy score, primary ranking metric). |
| `coherence_score` | FLOAT | Initial coherence relative to the array's history. |

## 3. The Cognitive Time Lattice (CTL)

The array operates on a multi-scale time lattice:

* **L0: Real-Time Stream (Micro-Scale):** Continuous ingestion and $9.4$ second decay monitoring.
* **L1: Daily Collision Epoch (Meso-Scale):** The $24$-hour period culminating in the $collider.py$ run.
* **L2: Supra-Individual Observation (Macro-Scale):** Observation of persistent $Cognitive\ Meson$ patterns.

## 4. Sub-Protocol: Proof of Thought (PoT)

The PoT mechanism validates the **Negative Entropy** score ($-\Delta S$) via consensus scoring from the multi-AI fusion engine, ensuring the Cogniton is truly novel and high-energy.

---
*This protocol is subject to rapid change until the launch of CogniChain v1.0.*