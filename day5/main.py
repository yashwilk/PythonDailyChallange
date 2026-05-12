"""This is a graph cycle detection problem.Course Schedule"""
"""You have 4 courses (0–3) and a list of prerequisites. An arrow from A → B means "take A before B". Can you find an order to complete all courses?
course0-course1-course2
|
course3

0 → 1 → 2, and also 0 → 3. Valid order: take 0, then 1 and 3, then 2."""


#numCourses = 4

#prerequisites = [
#    [0,1],[0,3],[1,2]]

#take 0 befor 1, take 0 before 3 take 1 before 2
"""0,1,2,3
firt 0 is gray and resta are white
next 1 is gray 
next 2 is gray - 2 becomes green - 1 becomes green
next 3 becomes gray
next 3 becoems green"""



def finishcourse(numCourses,prerequisite):
    graph={i:[] for i in range(prerequisite)} #give each course empty box to sotre its neighbours
    for a,b in prerequisite:
        graph[a].append(b) # for check what to check after 1st course
    color=[0]*numCourses # make all the course white

    def dfs(node):
        if color[node]==1:return False  # is the course grey
        if color[node]==2: return True  # is the course green
        color[node]=1                   # its a grey 
        for neighbour in graph[node]:       # go chekc the neighbours of this node
            if not dfs(neighbour): return False #if the df return fase th ereturn false again
        color[node]=2 # if all neighbours are safe the retun green
        return True

    return all(dfs(i) for i in range(numCourses))






import pandas as pd
# Sample dataset
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Alice", "David"],
    "Age": [25, 30, 25, 40]
})


duplicates=df[df.duplicated()]
print(duplicates)


remove_duplicates=df.drop_duplicates()
print(remove_duplicates)