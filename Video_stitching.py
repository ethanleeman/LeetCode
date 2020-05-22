class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        current_num_clips = 0
        current_time = 0
        while(current_time < T):
            best = current_time
            for L in clips:
                if (L[0] <= current_time):
                    if (L[1] > best):
                        best = L[1]
            if (best == current_time):
                return -1
            current_num_clips += 1
            current_time = best
        return current_num_clips
            
