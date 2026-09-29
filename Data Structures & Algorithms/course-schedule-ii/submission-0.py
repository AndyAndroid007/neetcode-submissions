class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0]*numCourses
        adj_list = {i:[] for i in range(numCourses)}
        for course,prereq in prerequisites:
            inDegree[course] += 1
            adj_list[prereq].append(course)
        
        final = []

        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
                final.append(i)
        count = 0
        while q:
            prereq = q.popleft()
            final.append(prereq)
            count += 1
            for course in adj_list[prereq]:
                inDegree[course]-=1
                if inDegree[course] == 0:
                    q.append(course)        
        
        if count < numCourses:
            return []
        
        return final
        
        