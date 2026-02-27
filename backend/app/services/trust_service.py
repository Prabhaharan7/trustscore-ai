class TrustService:
    @staticmethod
    def calculate_new_trust_score(old_trust_score: float, risk_score: float) -> float:
        """
        Calculate the updated trust score based on the risk score of an attempt.
        
        Formula: new_trust_score = old_trust_score - (risk_score / 10)
        Ensures the score never drops below 0.
        
        Args:
            old_trust_score: The user's current trust score.
            risk_score: The calculated risk score from their latest attempt.
            
        Returns:
            float: The updated trust score (minimum 0.0).
        """
        deduction = risk_score / 10.0
        new_trust_score = float(old_trust_score) - deduction
        
        # Ensure trust score never goes below 0
        return max(0.0, float(new_trust_score))

# Export a default instance if needed
trust_service = TrustService()
