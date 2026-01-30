"""
Main entry point for the Fitness Data Assistant.
Demo script for hackathon presentation.
"""
import os
from dotenv import load_dotenv
from openai import OpenAI

from .data_loader import load_and_normalize_csv
from .router import handle_user_query


def main():
    """
    Demo flow:
    1. Load environment variables
    2. Initialize OpenAI client
    3. Load and normalize CSV data
    4. Interactive query loop
    """
    # Load API key from .env
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        print("Error: OPENAI_API_KEY not found in .env file")
        return
    
    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Load workout data
    csv_path = "data/workouts.csv"  # Update with actual path
    print(f"Loading data from {csv_path}...")
    
    try:
        df = load_and_normalize_csv(csv_path)
        print(f"Loaded {len(df)} workout records")
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return
    
    # Interactive loop
    print("\n" + "="*50)
    print("Fitness Data Assistant")
    print("="*50)
    print("Ask questions about your workout data!")
    print("Type 'quit' to exit\n")
    
    while True:
        query = input("You: ").strip()
        
        if query.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
            
        if not query:
            continue
            
        try:
            response = handle_user_query(query, df, client)
            print(f"\nAssistant: {response}\n")
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
