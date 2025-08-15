#!/usr/bin/env python3
"""
ETL Agent CLI - Run the data enrichment pipeline
"""
from dotenv import load_dotenv
import os
import sys

# Load environment variables
load_dotenv()

# Check for required environment variables
if not os.getenv("OPENAI_API_KEY"):
    print("❌ Error: OPENAI_API_KEY not found in environment variables")
    print("Please set your OpenAI API key in the .env file")
    sys.exit(1)

from graph import etl_app

def main():
    """Run the ETL pipeline."""
    print("🚀 Starting ETL Agent...")
    print("=" * 50)
    
    try:
        # Run the ETL pipeline
        result = etl_app.invoke({})
        
        print("=" * 50)
        print("✅ ETL Pipeline completed successfully!")
        print(f"📊 Final state contains {len(result.get('rows', []))} processed rows")
        
    except FileNotFoundError as e:
        print(f"❌ File Error: {e}")
        print("Make sure the input file exists in raw_data/users.jsonl")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ Pipeline Error: {e}")
        print("Check your configuration and try again")
        sys.exit(1)

if __name__ == "__main__":
    main()
