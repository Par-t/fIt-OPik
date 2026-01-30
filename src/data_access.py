"""
Data access layer for DataFrame queries.
Handles DATA_ACCESS intent - filtering and returning workout data.
"""
import pandas as pd
from .config import EXERCISE_MUSCLE_MAP


def extract_target(query: str, client) -> dict:
    """
    Extract exercise or muscle target from user query using LLM.
    
    Args:
        query: User's natural language query
        client: OpenAI client instance
        
    Returns:
        Dict with keys:
        - type: "exercise" | "muscle" | "all"
        - value: exercise_id or muscle name or None
        
    Examples:
        "Show bench press history" -> {"type": "exercise", "value": "bench_press"}
        "List all chest exercises" -> {"type": "muscle", "value": "chest"}
        "Show all my workouts" -> {"type": "all", "value": None}
    """
    # TODO: Implement
    # 1. Use LLM to extract what the user is asking about
    # 2. Match to exercise_id or muscle name
    pass


def get_exercise_history(
    df: pd.DataFrame,
    exercise_id: str = None,
    muscle: str = None,
    limit: int = None
) -> pd.DataFrame:
    """
    Filter DataFrame by exercise or muscle.
    
    Args:
        df: Normalized workout DataFrame
        exercise_id: Filter by canonical exercise ID
        muscle: Filter by muscle (checks primary_muscle)
        limit: Max rows to return
        
    Returns:
        Filtered DataFrame
    """
    # TODO: Implement
    # 1. If exercise_id, filter df["exercise_id"] == exercise_id
    # 2. If muscle, filter df["primary_muscle"] == muscle
    # 3. Apply limit if provided
    # 4. Return filtered df
    pass


def format_history_response(df: pd.DataFrame) -> str:
    """
    Format DataFrame as readable text for user.
    
    Args:
        df: Filtered workout DataFrame
        
    Returns:
        Formatted string representation
    """
    # TODO: Implement
    # Simple tabular format or summary
    pass
