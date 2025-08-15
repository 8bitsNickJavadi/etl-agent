import json
import os

def save_node(state: dict) -> dict:
    """Save enriched data to output file."""
    # Ensure outputs directory exists
    os.makedirs("outputs", exist_ok=True)
    
    output_file = "outputs/enriched.jsonl"
    rows = state.get("rows", [])
    
    if not rows:
        print("Warning: No rows to save")
        return state
    
    with open(output_file, "w") as f:
        for row in rows:
            f.write(json.dumps(row) + "\n")
    
    print(f"✅ Saved {len(rows)} enriched rows to {output_file}")
    return state
