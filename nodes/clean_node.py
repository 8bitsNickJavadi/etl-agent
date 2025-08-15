def clean_node(state: dict) -> dict:
    """Clean and sanitize the loaded data."""
    cleaned = []
    
    for row in state["rows"]:
        # Create a copy to avoid modifying original
        cleaned_row = row.copy()
        
        # Clean bio field
        cleaned_row["bio"] = cleaned_row.get("bio", "").strip()
        
        # Clean name field
        cleaned_row["name"] = cleaned_row.get("name", "").strip()
        
        # Skip rows with empty required fields
        if not cleaned_row["name"] or not cleaned_row["bio"]:
            print(f"Warning: Skipping row with missing name or bio: {cleaned_row}")
            continue
            
        cleaned.append(cleaned_row)
    
    state["rows"] = cleaned
    print(f"Cleaned {len(cleaned)} rows (removed {len(state.get('rows', [])) - len(cleaned)} invalid rows)")
    return state
