"""
RAG pipeline for REASONING intent.
Generates derived facts from data and produces LLM-powered advice.
"""
import pandas as pd
from openai import OpenAI


def generate_exercise_facts(df: pd.DataFrame, exercise_id: str = None) -> list[str]:
    """
    Generate derived facts from workout data for RAG context.
    
    Args:
        df: Normalized workout DataFrame
        exercise_id: Optional filter for specific exercise
        
    Returns:
        List of factual statements like:
        - "User performed bench_press 12 times in the last 4 weeks"
        - "Bench press PR: 100kg x 5 reps on 2024-01-15"
        - "Weekly volume trend: increasing (+15% over 4 weeks)"
        - "Average rest between bench sessions: 3.2 days"
        
    Notes:
        These facts are the RAG context - LLM never sees raw CSV rows
    """
    # TODO: Implement
    # 1. Filter to exercise if provided
    # 2. Calculate aggregates:
    #    - Total sessions / frequency
    #    - PR detection (max weight * reps)
    #    - Weekly volume trends
    #    - Recent performance
    # 3. Convert to natural language statements
    pass


def generate_advice(
    query: str,
    facts: list[str],
    client: OpenAI
) -> str:
    """
    Generate personalized training advice using RAG.
    
    Args:
        query: User's original question
        facts: List of derived facts from their data
        client: OpenAI client instance
        
    Returns:
        LLM-generated advice grounded in the user's data
        
    Notes:
        - LLM receives facts, not raw data
        - Response should include 1-2 concrete recommendations
    """
    # TODO: Implement
    # 1. Build system prompt (fitness coach persona)
    # 2. Include facts as context
    # 3. Include user query
    # 4. Generate response with recommendations
    pass
