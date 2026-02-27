class SkillAnalyzer:
    """
    A service class responsible for calculating problem solving, logic,
    and efficiency scores based on code submission metrics.
    """

    @staticmethod
    def analyze_submission(
        time_taken: int, 
        code_length: int, 
        test_cases_passed: int, 
        total_test_cases: int
    ) -> dict[str, float]:
        """
        Calculate various skill scores based on code submission data.
        
        Args:
            time_taken: Time taken to submit the code in seconds.
            code_length: The length of the submitted code in characters.
            test_cases_passed: The number of test cases passed.
            total_test_cases: The total number of test cases for the problem.
            
        Returns:
            A dictionary containing problem_solving_score, logic_score, and efficiency_score.
        """
        
        # Edge case: Avoid division by zero
        if total_test_cases == 0:
            return {
                "problem_solving_score": 0.0,
                "logic_score": 0.0,
                "efficiency_score": 0.0
            }

        # 1. Logic Score (0-100)
        # Driven entirely by how many test cases passed vs the total available.
        logic_ratio = float(test_cases_passed) / float(total_test_cases)
        logic_score = round(logic_ratio * 100.0, 2)

        # 2. Problem Solving Score (0-100)
        # Driven by logic score, but partially penalized by taking too long.
        # Assume a baseline "expected max time" of 3600 seconds (1 hour).
        time_penalty = min(time_taken / 3600.0 * 20.0, 20.0) # Up to 20 point penalty for taking an hour+
        
        # If they didn't pass anything, they haven't solved the problem
        if test_cases_passed == 0:
            problem_solving_score = 0.0
        else:
            problem_solving_score = max(logic_score - time_penalty, 0.0)
            
        problem_solving_score = round(problem_solving_score, 2)

        # 3. Efficiency Score (0-100)
        # Driven by logic score + code conciseness.
        # Assume a "bloated code" penalty mapping over 2000 chars.
        if test_cases_passed == 0:
            efficiency_score = 0.0
        else:
            # Short code = better efficiency rating (up to a reasonable baseline).
            # Over 2000 characters gives a flat penalty.
            char_penalty = min(code_length / 2000.0 * 15.0, 15.0) 
            efficiency_score = max(logic_score - char_penalty, 0.0)
            
        efficiency_score = round(efficiency_score, 2)

        return {
            "problem_solving_score": problem_solving_score,
            "logic_score": logic_score,
            "efficiency_score": efficiency_score
        }
