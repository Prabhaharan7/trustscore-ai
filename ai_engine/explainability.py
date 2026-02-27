from typing import Any, Dict

class ExplainabilityEngine:
    """
    Translates raw behavioral metrics and the final risk score into
    a structured, human-readable format suitable for auditing.
    """

    @staticmethod
    def generate_risk_explanation(
        tab_switch_count: int,
        face_absent_seconds: int,
        code_similarity: float,
        copy_paste_count: int,
        multiple_faces_detected: bool,
        risk_score: float
    ) -> Dict[str, Any]:
        """
        Generate a structured dictionary explaining the contributing factors
        to the given risk score.
        
        Args:
            tab_switch_count: Number of times user switched away from the tab.
            face_absent_seconds: Seconds user's face was absent.
            code_similarity: Percentage of matching code.
            copy_paste_count: Number of copy-paste actions.
            multiple_faces_detected: Whether multiple faces were observed.
            risk_score: The final computed risk score.
            
        Returns:
            Dict containing total score, contributing factors Breakdown, and a human-readable summary.
        """
        # Define the individual contributions based on the established formula weights
        # (This matches the weighting from RiskCalculator)
        tab_switch_contribution = tab_switch_count * 10
        face_absent_contribution = face_absent_seconds * 2
        code_similarity_contribution = round(code_similarity * 0.5, 2)
        copy_paste_contribution = copy_paste_count * 5
        multiple_faces_contribution = 25 if multiple_faces_detected else 0

        contributing_factors = {}
        explanations = []

        if tab_switch_count > 0:
            contributing_factors["tab_switches"] = {
                "count": tab_switch_count,
                "risk_contribution": tab_switch_contribution
            }
            explanations.append(f"Tab switching occurred {tab_switch_count} times (+{tab_switch_contribution} risk).")

        if face_absent_seconds > 0:
            contributing_factors["face_absence"] = {
                "seconds": face_absent_seconds,
                "risk_contribution": face_absent_contribution
            }
            explanations.append(f"Face absent for {face_absent_seconds} seconds (+{face_absent_contribution} risk).")

        if code_similarity > 0.0:
            contributing_factors["code_similarity"] = {
                "percentage": code_similarity,
                "risk_contribution": code_similarity_contribution
            }
            explanations.append(f"Code similarity of {code_similarity}% (+{code_similarity_contribution} risk).")

        if copy_paste_count > 0:
            contributing_factors["copy_paste"] = {
                "count": copy_paste_count,
                "risk_contribution": copy_paste_contribution
            }
            explanations.append(f"Copy-paste used {copy_paste_count} times (+{copy_paste_contribution} risk).")

        if multiple_faces_detected:
            contributing_factors["multiple_faces"] = {
                "detected": True,
                "risk_contribution": multiple_faces_contribution
            }
            explanations.append(f"Multiple faces detected (+{multiple_faces_contribution} risk).")

        if not explanations:
            human_readable_explanation = "No suspicious behavior detected."
        else:
            human_readable_explanation = "Risk factors detected: " + " ".join(explanations)

        return {
            "total_risk_score": risk_score,
            "contributing_factors": contributing_factors,
            "human_readable_explanation": human_readable_explanation
        }
