class Boggle:
    def __init__(self, grid, dictionary): 
        self.grid = grid if grid else [] # Use an empty list if no grid is passed
        self.dictionary = set(dictionary) if dictionary else set() # Use an empty set if no dictionary is passed
        self.solution = set() #Used to avoid duplicate words
      

    # Setter for grid and dictionary
    def setGrid(self, grid):
      """Setter for grid."""
      self.grid = grid
    
    def setDictionary(self, dictionary):
      """Setter for the dictionary."""
      self.dictionary = set(dictionary)
    
    def getSolution(self):
      """Getter for the solution. Returns found words."""
      return self.solution
  
    def boggleGame(self):
      """Finds all the valid words from the grid."""
      if not self.grid or not self.dictionary:
        return 
      self.rows = len(self.grid)
      self.columns = len(self.grid[0])
      visited = []
      for _ in range(self.rows):
        visited.append([False] * self.columns)
      for r in range(self.rows):
        for c in range(self.columns):
          self.dfs(r, c, "", visited)

    def dfs(self, r, c, path, visited):
      """Performs Depth First Search to find all valid words starting from (r, c)."""
      if r < 0 or r >= self.rows or c < 0 or c >= self.columns or visited[r][c]:
        return 
      path += self.grid[r][c]
      if not self.wordPrefix(path):
        return 
      if len(path) > 3 and path in self.dictionary:
        self.solution.add(path)
      visited[r][c] = True
      direction = [
                      (-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1)
                    ]
      for rs, cs in direction:
        next_r, next_c = r + rs, c + cs
        self.dfs(next_r, next_c, path, visited)
      visited[r][c] = False

    def wordPrefix(self, words):
      """ To check if the current word is a prefix of any dictionary word."""
      for word in self.dictionary:
        if word.startswith(words):
          return True
      return False

def main():
    grid = [['A', 'B', 'C', 'D'],
            ['E', 'F', 'G', 'H'], 
            ['I', 'J', 'K', 'L'], 
            ['A', 'B', 'C', 'D']]
    dictionary = ['ABEF', 'AFJIEB', 'DGKD', 'DGKA']
    mygame = Boggle(grid, dictionary)
    mygame.boggleGame()
    print(mygame.getSolution())
if __name__ == "__main__":
    main()
