class RiskCalculator:
    """
    A service class responsible for calculating trust risk scores
    based on various behavioral metrics gathered during an assessment.
    """

    @staticmethod
    def calculate_risk_score(
        tab_switch_count: int = 0,
        face_absent_seconds: int = 0,
        code_similarity: float = 0.0,
        copy_paste_count: int = 0,
        multiple_faces_detected: bool = False
    ) -> float:
        """
        Calculate the risk score of an expected attempt based on behavioral factors.
        Risk score is capped at a maximum of 100.
        
        Args:
            tab_switch_count: Number of times the user switched away from the assessment tab.
            face_absent_seconds: Total seconds the user's face was not detected in the camera.
            code_similarity: Percentage of code similarity matching against references (0.0 - 100.0).
            copy_paste_count: Number of times copy-paste actions were detected.
            multiple_faces_detected: True if more than one face was seen during the assessment.
            
        Returns:
            float: The calculated risk score, capped between 0 and 100.
        """
        # Define the weight multipliers for the risk formula
        TAB_SWITCH_WEIGHT = 10
        FACE_ABSENT_WEIGHT = 2
        CODE_SIMILARITY_WEIGHT = 0.5
        COPY_PASTE_WEIGHT = 5
        MULTIPLE_FACES_PENALTY = 25

        # Calculate the base score using the given formula
        base_risk = (tab_switch_count * TAB_SWITCH_WEIGHT) + \
                    (face_absent_seconds * FACE_ABSENT_WEIGHT) + \
                    (code_similarity * CODE_SIMILARITY_WEIGHT) + \
                    (copy_paste_count * COPY_PASTE_WEIGHT)

        # Apply flat penalty if multiple faces are detected
        if multiple_faces_detected:
            base_risk += MULTIPLE_FACES_PENALTY

        # Cap the risk score at a maximum of 100.0, and a minimum of 0.0
        final_risk_score = min(max(base_risk, 0.0), 100.0)

        return float(final_risk_score)
