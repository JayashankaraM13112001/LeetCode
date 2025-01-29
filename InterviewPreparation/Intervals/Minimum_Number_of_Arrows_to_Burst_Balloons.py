class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        arrows = 1
        arrow_pos = points[0][1]

        for xstart, xend in points[1:]:
            if xstart > arrow_pos:  
                arrows += 1
                arrow_pos = xend
        return arrows