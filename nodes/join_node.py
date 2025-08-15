def join_node(state: dict) -> dict:
    """Join fan-out results back into the main state."""
    # Fan-out output gets stored under "fanout" key
    enriched_rows = state.get("fanout", [])
    
    if not enriched_rows:
        print("Warning: No enriched rows found in fanout results")
        state["rows"] = []
    else:
        state["rows"] = enriched_rows
        print(f"Joined {len(enriched_rows)} enriched rows")
    
    return state
