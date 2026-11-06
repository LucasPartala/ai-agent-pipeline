"""
Autonomous AI Lead Scoring & Dispatch Pipeline
Author: Lucas Partala
Description: Autonomous agent that scores business opportunities and triggers action webhooks.
"""

import json
from dataclasses import dataclass
from typing import Dict, Any, List

@dataclass
class ScoredLead:
    business_name: str
    category: str
    opportunity_score: float  # Scale 1-10
    reasoning: str
    action_required: bool

class AIAgentScoringEngine:
    def __init__(self, score_threshold: float = 7.0):
        self.score_threshold = score_threshold

    def evaluate_lead(self, lead_data: Dict[str, Any]) -> ScoredLead:
        """Evaluates business opportunity based on rating, digital presence and reviews."""
        has_website = bool(lead_data.get("website"))
        rating = float(lead_data.get("rating", 0.0))
        reviews = int(lead_data.get("reviews_count", 0))

        # Heuristic scoring logic
        score = 5.0
        reasons = []

        if not has_website and rating >= 4.0:
            score += 3.5
            reasons.append("High rating but no website: Prime candidate for automated landing page.")
        
        if reviews > 50:
            score += 1.5
            reasons.append("Established customer base with high transaction volume.")

        score = min(10.0, score)
        action_required = score >= self.score_threshold

        return ScoredLead(
            business_name=lead_data.get("name", "Unknown"),
            category=lead_data.get("category", "General"),
            opportunity_score=round(score, 1),
            reasoning=" | ".join(reasons) if reasons else "Standard business profile.",
            action_required=action_required
        )

    def dispatch_webhook(self, scored_lead: ScoredLead):
        """Simulates webhook notification for qualified leads."""
        payload = {
            "event": "HIGH_VALUE_OPPORTUNITY_DETECTED",
            "business": scored_lead.business_name,
            "score": scored_lead.opportunity_score,
            "reasoning": scored_lead.reasoning
        }
        print(f"[DISPATCH WEBHOOK] -> Qualified: {scored_lead.business_name} (Score: {scored_lead.opportunity_score}/10)")

if __name__ == "__main__":
    print("[*] Running Autonomous AI Lead Scoring Pipeline...")
    agent = AIAgentScoringEngine()

    test_leads = [
        {"name": "Elite Orthodontics", "category": "Dentist", "rating": 4.8, "reviews_count": 87, "website": ""},
        {"name": "Downtown Bakery", "category": "Food", "rating": 3.2, "reviews_count": 12, "website": "https://example.com"},
    ]

    for lead in test_leads:
        result = agent.evaluate_lead(lead)
        if result.action_required:
            agent.dispatch_webhook(result)
        else:
            print(f"[ARCHIVED] -> Low Opportunity: {result.business_name} (Score: {result.opportunity_score}/10)")
