class RiskService:
    @staticmethod
    def calculate_risk_score(
        tab_switch_count: int = 0,
        face_absent_seconds: int = 0,
        code_similarity: float = 0.0
    ) -> float:
        """
        Calculate the risk score of an assessment attempt based on behavior metrics.
        
        Args:
            tab_switch_count: Number of times the user switched away from the assessment tab.
            face_absent_seconds: Total seconds the user's face was not detected.
            code_similarity: Percentage of code similarity to known sources (0.0 to 100.0).
            
        Returns:
            float: The calculated risk score.
        """
        # Risk formula weights
        TAB_SWITCH_WEIGHT = 10
        FACE_ABSENT_WEIGHT = 2
        CODE_SIMILARITY_WEIGHT = 0.5
        
        base_risk = (tab_switch_count * TAB_SWITCH_WEIGHT) + \
                    (face_absent_seconds * FACE_ABSENT_WEIGHT) + \
                    (code_similarity * CODE_SIMILARITY_WEIGHT)
                    
        # Optional: Normalize or cap the score if needed
        # risk_score = min(max(base_risk, 0.0), 100.0)
        
        return float(base_risk)

# Export a default instance if needed, though static methods make it optional
risk_service = RiskService()
