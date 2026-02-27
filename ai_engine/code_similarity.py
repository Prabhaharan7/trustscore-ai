import difflib

class CodeSimilarityAnalyzer:
    """
    A service class configured to analyze the similarity between two distinct pieces of code.
    Currently uses string-based similarity, but is designed to be easily swappable
    with an AST-based analyzer for deeper logical comparison in the future.
    """

    @staticmethod
    def calculate_similarity(code1: str, code2: str) -> float:
        """
        Calculate a similarity ratio percentage between two code snippets.
        
        Args:
            code1 (str): The first code snippet.
            code2 (str): The second code snippet (e.g., a reference solution or past submission).
            
        Returns:
            float: A percentage representing string similarity, restricted from 0.0 to 100.0.
        """
        # Edge case: If both are empty strings, they are perfectly similar
        if not code1 and not code2:
            return 100.0
            
        # Edge case: If only one is an empty string, they are completely different
        if not code1 or not code2:
            return 0.0

        # difflib.SequenceMatcher.ratio() returns a float in [0, 1]
        # representing the similarity of the two sequences.
        matcher = difflib.SequenceMatcher(None, code1, code2)
        ratio = matcher.ratio()
        
        # Convert to a percentage string format, rounded to 2 decimal points, then back to float
        similarity_percentage = round(ratio * 100.0, 2)
        
        return similarity_percentage
