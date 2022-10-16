"""
You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. Multiple points can have the same coordinates.

You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.

For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are considered inside.

Return an array answer, where answer[j] is the answer to the jth query.
"""

from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        for query in queries:
            count = 0
            for point in points:
                if ((query[0] - point[0]) ** 2) + ((query[1] - point[1]) ** 2) <= query[2] ** 2:
                    count += 1
            result.append(count)
        return result
