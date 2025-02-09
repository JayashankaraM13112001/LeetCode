'''There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.'''

class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Step 1: Build adjacency list
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # Step 2: DFS function with cycle detection
        visit = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = fully processed
        
        def dfs(course):
            if visit[course] == 1:  # Cycle detected
                return False
            if visit[course] == 2:  # Already processed
                return True
            
            visit[course] = 1  # Mark as visiting
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            
            visit[course] = 2  # Mark as fully processed
            return True
        
        # Step 3: Check all courses
        for course in range(numCourses):
            if visit[course] == 0:
                if not dfs(course):
                    return False
        
        return True
