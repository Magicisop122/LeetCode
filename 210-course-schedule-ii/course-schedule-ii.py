class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        prereq = {i : [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        # course has 3 states
        # visited -> added to the output
        # visiting -> not added to the output and currently in the cycle
        # unvisited 
        output = []
        visited, visiting =  set(), set()

        def dfs(crs):
            if crs in visiting:
                return False    # we have a cycle
            if crs in visited:
                return True     # that means we can complete this course
            
            visiting.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            
            visiting.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []

        return output
