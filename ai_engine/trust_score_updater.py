class TrustUpdater:
    """
    A service class responsible for safely updating user trust scores
    based on the risk score generated during an assessment.
    """

    @staticmethod
    def update_trust_score(old_trust_score: float, risk_score: float) -> float:
        """
        Calculate the new trust score by deducting a scaled risk score.
        
        Formula: new_trust_score = old_trust_score - (risk_score / 10)
        
        Rules applied:
        - The resulting trust score will never fall below 0.0.
        - The resulting trust score will never exceed 100.0.
        
        Args:
            old_trust_score: The user's current trust score before this calculation.
            risk_score: The risk score calculated from the assessment attempt.
            
        Returns:
            float: The updated trust score, strictly bounded between 0.0 and 100.0.
        """
        # Calculate the deduction logic
        deduction = risk_score / 10.0
        new_score = old_trust_score - deduction
        
        # Ensure the score stays within the valid [0.0, 100.0] range
        bounded_score = min(max(new_score, 0.0), 100.0)
        
        return float(bounded_score)
