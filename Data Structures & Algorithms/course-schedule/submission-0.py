class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0]*numCourses
        adj_list = {i:[] for i in range(numCourses)}
        for course,prereq in prerequisites:
            inDegree[course] += 1
            adj_list[prereq].append(course)
        
        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        count = 0
        while q:
            prereq = q.popleft()
            count += 1
            for course in adj_list[prereq]:
                inDegree[course]-=1
                if inDegree[course] == 0:
                    q.append(course)
        return count == numCourses
            

        

        