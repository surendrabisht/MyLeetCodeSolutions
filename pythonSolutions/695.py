class Solution:
    def __init__(self) -> None:
        self.discovered_vertices=[]
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        cols=len(grid[0])
        self.discovered_vertices=[0]*len(grid)

        for i in range(len(grid)):
            self.discovered_vertices[i]=[]
            self.discovered_vertices[i]=[0]*cols

        island_max_area=0
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if self.discovered_vertices[row][column]!=1:
                    area=self.get_island_length(grid,row,column)
                    if island_max_area<area:
                        island_max_area=area
        
        return island_max_area
                


    def get_island_length(self,grid: list[list[int]],x:int,y:int) -> int:
        count =0
        if self.discovered_vertices[x][y]!=1:
            self.discovered_vertices[x][y]=1
            x_length= len(grid)
            y_length= len(grid[0])
            if grid[x][y]==1:
                count=1
                if x>0:
                    count += self.get_island_length(grid,x-1,y)
                if x<x_length-1:
                    count += self.get_island_length(grid,x+1,y)
                if y>0:
                    count += self.get_island_length(grid,x,y-1)
                if y<y_length -1:
                    count += self.get_island_length(grid,x,y+1)            
        return count
        
        


if __name__ =="__main__":
    input = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(Solution().maxAreaOfIsland(input))


        