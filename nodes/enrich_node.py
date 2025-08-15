from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import json
import os

# Initialize LLM
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

PROMPT = ChatPromptTemplate.from_template("""
Given this person's bio: "{bio}", return a JSON object with:
- category (e.g., 'Product', 'Research', 'Finance', 'Engineering', 'Marketing', 'Founder', etc.)
- tags (3-6 relevant keywords)
- location (city, country if mentioned or can be inferred)
- seniority (e.g., 'Senior', 'Entry', 'Mid-level', 'Executive')

Respond with ONLY valid JSON, no additional text.

Example:
{{"category": "Product", "tags": ["climate tech", "product management", "Google X"], "location": "USA", "seniority": "Senior"}}
""")

def enrich_node(single_row: dict) -> dict:
    """Enrich a single row with LLM-generated metadata."""
    bio = single_row.get("bio", "")
    
    if not bio.strip():
        # Return default values for empty bio
        enriched = {
            "category": "Unknown",
            "tags": [],
            "location": "Unknown",
            "seniority": "Unknown"
        }
    else:
        try:
            prompt = PROMPT.format(bio=bio)
            response = llm.invoke(prompt)
            raw_content = response.content.strip()
            
            # Try to parse JSON response
            enriched = json.loads(raw_content)
            
            # Validate required fields
            required_fields = ["category", "tags", "location", "seniority"]
            for field in required_fields:
                if field not in enriched:
                    enriched[field] = "Unknown" if field != "tags" else []
                    
        except json.JSONDecodeError as e:
            print(f"Warning: Failed to parse LLM response for {single_row.get('name', 'Unknown')}: {e}")
            enriched = {
                "category": "Unknown",
                "tags": [],
                "location": "Unknown", 
                "seniority": "Unknown"
            }
        except Exception as e:
            print(f"Warning: Error enriching {single_row.get('name', 'Unknown')}: {e}")
            enriched = {
                "category": "Unknown",
                "tags": [],
                "location": "Unknown",
                "seniority": "Unknown"
            }
    
    # Update the row with enriched data
    single_row.update(enriched)
    return single_row
