from typing import Any, Dict
from datetime import datetime

class ReportGenerator:
    """
    A service class configured to generate structured, human-readable 
    final reports for an assessment attempt. Suitable for rendering
    on admin dashboards or saving to an audit log.
    """

    @staticmethod
    def generate_final_report(
        user_id: int,
        final_score: float,
        risk_score: float,
        old_trust_score: float,
        new_trust_score: float,
        skill_scores: Dict[str, float],
        explanation: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Aggregate all metrics from an assessment into a cohesive JSON-style 
        dictionary report.
        
        Args:
            user_id: The ID of the user who took the assessment.
            final_score: The final objective grading score of the assessment.
            risk_score: The calculated AI risk score.
            old_trust_score: The user's trust score prior to this assessment.
            new_trust_score: The user's updated trust score.
            skill_scores: The dictionary output of SkillAnalyzer (logic, efficiency, problem solving).
            explanation: The dictionary output of ExplainabilityEngine.
            
        Returns:
            A structured report dictionary.
        """
        
        # Calculate the trust score delta (change in score)
        trust_score_change = round(new_trust_score - old_trust_score, 2)
        change_direction = "decreased" if trust_score_change < 0 else "increased" if trust_score_change > 0 else "unchanged"

        # Determine overall flag status for admin dashboard
        needs_review = risk_score >= 50.0  # Threshold can be configured later

        report = {
            "metadata": {
                "user_id": user_id,
                "generated_at": datetime.utcnow().isoformat() + "Z",
                "needs_mandatory_review": needs_review
            },
            "summary": {
                "assessment_score": final_score,
                "risk_rating": risk_score,
                "trust_standing": new_trust_score
            },
            "skill_analysis": {
                "problem_solving": skill_scores.get("problem_solving_score", 0.0),
                "logic": skill_scores.get("logic_score", 0.0),
                "efficiency": skill_scores.get("efficiency_score", 0.0)
            },
            "risk_analysis": {
                "score": risk_score,
                "explanation_summary": explanation.get("human_readable_explanation", "No explanation provided."),
                "breakdown": explanation.get("contributing_factors", {})
            },
            "trust_impact": {
                "previous_score": old_trust_score,
                "new_score": new_trust_score,
                "change": trust_score_change,
                "trend": change_direction
            }
        }
        
        return report
