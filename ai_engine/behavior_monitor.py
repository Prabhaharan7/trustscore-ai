import time
from typing import Dict, Any

class BehaviorMonitor:
    """
    A service class configured to track user behavior during an assessment.
    Monitors face presence, absence duration, and multiple faces detections.
    
    Note: OpenCV integration logic is currently acting as a placeholder 
          to be implemented by actual computer vision modules parsing feeds.
    """

    def __init__(self):
        # Current status flags
        self.face_detected: bool = True
        self.multiple_faces_detected: bool = False
        
        # Accumulators and Trackers
        self.face_absent_duration: int = 0
        self._last_absence_start_time: float = 0.0

    def update_face_status(self, face_present: bool) -> None:
        """
        Update the current face detection status and calculate absence duration.
        
        Args:
            face_present (bool): True if a face is currently detected in the frame.
        """
        # If the state changed from present -> absent
        if not face_present and self.face_detected:
            self._last_absence_start_time = time.time()
            
        # If the state changed from absent -> present
        elif face_present and not self.face_detected:
            # Add the duration of the recent absence block to the total accumulator
            absence_block = time.time() - self._last_absence_start_time
            self.face_absent_duration += int(absence_block)
            
        self.face_detected = face_present

    def update_multiple_faces(self, status: bool) -> None:
        """
        Update the flag if multiple faces are currently detected.
        
        Args:
            status (bool): True if more than one face is detected.
        """
        if status:
            self.multiple_faces_detected = True

    def get_behavior_summary(self) -> Dict[str, Any]:
        """
        Return the final accumulated metrics.
        This closes out any ongoing absence duration before returning the totals.
        
        Returns:
            Dict containing face present flag, total absent seconds, and multiple faces flag.
        """
        # If they are currently still absent when the summary is pulled, calculate the final gap
        if not self.face_detected:
            absence_block = time.time() - self._last_absence_start_time
            self.face_absent_duration += int(absence_block)
            self._last_absence_start_time = time.time() # Reset clock so it isn't double-counted

        return {
            "is_currently_detected": self.face_detected,
            "total_absent_seconds": self.face_absent_duration,
            "multiple_faces_detected": self.multiple_faces_detected
        }

    # ==========================================
    # Placeholder for OpenCV / Real Vision logic
    # ==========================================
    def process_vision_frame(self, frame) -> None:
        """
        [MOCK] Process a video frame from OpenCV or a webcam stream.
        This would be responsible for calling self.update_face_status()
        and self.update_multiple_faces() under the hood.
        """
        pass
