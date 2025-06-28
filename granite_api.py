# granite_api.py
import time
from typing import Tuple
import random

def transcribe_audio(audio_bytes: bytes) -> str:
    """Simulate transcription with realistic processing"""
    time.sleep(1.5)  # Simulate processing time
    sample_transcripts = [
        "The team discussed the Q3 marketing strategy, focusing on social media campaigns and influencer partnerships. John suggested increasing the budget by 15% for TikTok ads, while Sarah recommended prioritizing Instagram Reels. Action items were assigned for the next sprint.",
        "Technical review meeting covered the new API architecture. Backend team confirmed the endpoints will be ready by Friday. Frontend needs to update their mock data implementation. Security review scheduled for next Tuesday.",
        "Client feedback session for the new dashboard design. Users want more customization options and better mobile experience. Priority items: 1) Add theme selector 2) Improve chart loading speed 3) Redesign mobile navigation."
    ]
    return random.choice(sample_transcripts)

def summarize_text(transcript: str) -> Tuple[str, List[str]]:
    """Generate summary and action items with varied responses"""
    time.sleep(1)  # Simulate processing time
    
    summaries = {
        "marketing": "Discussed Q3 marketing strategy with focus on social media. Budget adjustments and platform prioritization needed.",
        "technical": "Reviewed API architecture progress. Coordination needed between frontend and backend teams before security review.",
        "design": "Collected client feedback on dashboard. Mobile experience and customization options identified as key improvement areas."
    }
    
    action_items = {
        "marketing": [
            "Increase TikTok ad budget by 15% (John)",
            "Create Instagram Reels content calendar (Sarah)",
            "Research influencer partnership opportunities (Marketing Team)"
        ],
        "technical": [
            "Finalize API endpoints by Friday (Backend)",
            "Update frontend mock data implementation (Frontend)",
            "Prepare documentation for security review (Tech Lead)"
        ],
        "design": [
            "Implement theme selector (UI Team)",
            "Optimize chart loading performance (Dev Team)",
            "Redesign mobile navigation (UX Team)"
        ]
    }
    
    # Determine context
    if "marketing" in transcript.lower():
        context = "marketing"
    elif "technical" in transcript.lower() or "api" in transcript.lower():
        context = "technical"
    else:
        context = "design"
    
    return summaries[context], action_items[context]