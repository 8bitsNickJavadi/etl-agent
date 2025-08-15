import json
import os

def load_node(state: dict) -> dict:
    """Load raw data from JSONL file into state."""
    file_path = "raw_data/users.jsonl"
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file {file_path} not found")
    
    rows = []
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError as e:
                    print(f"Warning: Skipping invalid JSON line: {line}")
                    continue
    
    state["rows"] = rows
    print(f"Loaded {len(rows)} rows from {file_path}")
    return state
