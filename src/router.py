"""
Query router - routes user queries based on classified intent.
Main orchestration logic.
"""
import pandas as pd
from openai import OpenAI

from .config import Intent
from .intent_classifier import classify_intent_llm
from .data_access import extract_target, get_exercise_history, format_history_response
from .rag_pipeline import generate_exercise_facts, generate_advice


def handle_user_query(query: str, df: pd.DataFrame, client: OpenAI) -> str:
    """
    Main entry point for handling user queries.
    
    Args:
        query: User's natural language query
        df: Normalized workout DataFrame (source of truth)
        client: OpenAI client instance
        
    Returns:
        Response string (either data table or LLM advice)
        
    Flow:
        1. Classify intent (DATA_ACCESS or REASONING)
        2. Route to appropriate handler
        3. Return formatted response
    """
    # TODO: Implement
    # 1. intent = classify_intent_llm(query, client)
    # 
    # 2. if intent == Intent.DATA_ACCESS:
    #        target = extract_target(query, client)
    #        history = get_exercise_history(df, ...)
    #        return format_history_response(history)
    #
    # 3. if intent == Intent.REASONING:
    #        target = extract_target(query, client)
    #        facts = generate_exercise_facts(df, target)
    #        return generate_advice(query, facts, client)
    pass
