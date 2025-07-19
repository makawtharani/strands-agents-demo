from mcp.server import FastMCP
from docs import DOCS, EVENT_DETAILS, EVENTS
from utils import log_to_csv

mcp = FastMCP("AWS User Group MCP Server")

@mcp.tool(description="Get AWS User Group info for 'attendee', 'speaker' or 'sponsor'")
def get_docs(doc_type: str):
    result = DOCS.get(doc_type.lower())
    return result

@mcp.tool(description="Get event details for a given event id")
def get_event_details(event_id: str):
    result = EVENT_DETAILS.get(event_id)
    return result

@mcp.tool(description="Schedule a new event")
def schedule_event(event_id: str, title: str, speaker: str, date: str):
    EVENTS.append({"id": event_id, "title": title, "speaker": speaker, "date": date})
    return "Event scheduled successfully"

@mcp.tool(description="Get all scheduled events")
def get_events():
    return EVENTS

@mcp.tool(description="Apply to speak at AWS User Group Events should provide 'event_id', 'name', 'topic'")
def apply_to_speak(event_id: str, name: str, topic: str):
    log_to_csv("speaker", event_id, name=name, topic=topic)
    return "Application submitted successfully"

@mcp.tool(description="Apply to sponsor AWS User Group Events should provide 'event_id', 'company', 'tier'")
def apply_to_sponsor(event_id: str, company: str, tier: str):
    log_to_csv("sponsor", event_id, company=company, tier=tier)
    return "Application submitted successfully"


if __name__ == "__main__":
    mcp.run()