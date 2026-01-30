"""
CSV ingestion and normalization.
Loads workout data and maps to canonical exercise IDs.
"""
import pandas as pd
from .config import EXERCISE_MUSCLE_MAP


def load_and_normalize_csv(filepath: str) -> pd.DataFrame:
    """
    Load CSV and normalize exercise data.
    
    Args:
        filepath: Path to the CSV file (e.g., Hevy export)
        
    Returns:
        Normalized DataFrame with columns:
        - exercise_title (original)
        - exercise_id (canonical)
        - primary_muscle
        - targeted_muscles
        - weight_kg
        - reps
        - start_time
        
    Notes:
        - Rows with unsupported exercises are dropped
        - Start time is converted to datetime
    """
    # TODO: Implement
    # 1. Read CSV with pandas
    # 2. Filter to only supported exercises (in EXERCISE_MUSCLE_MAP)
    # 3. Add exercise_id, primary_muscle, targeted_muscles columns
    # 4. Parse start_time to datetime
    # 5. Return cleaned DataFrame
    pass


def get_supported_exercises() -> list[str]:
    """Return list of supported exercise titles."""
    return list(EXERCISE_MUSCLE_MAP.keys())
