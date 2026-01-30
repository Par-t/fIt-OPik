"""
LLM-based intent classification.
Classifies user queries as DATA_ACCESS or REASONING.
"""
from openai import OpenAI
from .config import Intent


def classify_intent_llm(query: str, client: OpenAI) -> str:
    """
    Classify user query intent using LLM.
    
    Args:
        query: User's natural language query
        client: OpenAI client instance
        
    Returns:
        Intent.DATA_ACCESS or Intent.REASONING
        
    Examples:
        "Show me my bench press history" -> DATA_ACCESS
        "How can I improve my squat?" -> REASONING
        "List all chest exercises I did" -> DATA_ACCESS  
        "Why am I not progressing on deadlift?" -> REASONING
    """
    # TODO: Implement
    # 1. Create system prompt explaining the two intents
    # 2. Send query to LLM (gpt-4o-mini for cost efficiency)
    # 3. Parse response to return intent label
    pass
