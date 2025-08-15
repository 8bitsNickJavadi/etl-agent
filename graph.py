from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List
from nodes.load_node import load_node
from nodes.clean_node import clean_node
from nodes.enrich_node import enrich_node
from nodes.save_node import save_node

class ETLState(TypedDict):
    """State schema for the ETL pipeline."""
    rows: List[dict]

def fan_out_enrich(state: ETLState) -> dict:
    """Fan out enrichment: process each row individually."""
    enriched_rows = []
    
    print(f"Starting enrichment of {len(state['rows'])} rows...")
    
    for i, row in enumerate(state["rows"]):
        print(f"Enriching row {i+1}/{len(state['rows'])}: {row.get('name', 'Unknown')}")
        try:
            enriched_row = enrich_node(row.copy())
            enriched_rows.append(enriched_row)
        except Exception as e:
            print(f"Error enriching row {i+1}: {e}")
            # Add the original row with default enrichment
            row_copy = row.copy()
            row_copy.update({
                "category": "Unknown",
                "tags": [],
                "location": "Unknown",
                "seniority": "Unknown"
            })
            enriched_rows.append(row_copy)
    
    return {"rows": enriched_rows}

def create_etl_graph():
    """Create and configure the ETL StateGraph."""
    
    # Create the StateGraph
    graph = StateGraph(ETLState)
    
    # Add nodes
    graph.add_node("load", load_node)
    graph.add_node("clean", clean_node)
    graph.add_node("fan_out_enrich", fan_out_enrich)
    graph.add_node("save", save_node)
    
    # Add edges
    graph.add_edge(START, "load")
    graph.add_edge("load", "clean")
    graph.add_edge("clean", "fan_out_enrich")
    graph.add_edge("fan_out_enrich", "save")
    graph.add_edge("save", END)
    
    # Compile the graph
    return graph.compile()

# Create the compiled ETL application
etl_app = create_etl_graph()
