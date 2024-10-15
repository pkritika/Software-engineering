class Boggle:
  def __init__(self, grid, dictionary):
    #initialising the grid, dictionary and solution set
    self.grid = self.setGrid(grid)
    # print(self.grid)
    self.dictionary = [word.upper() for word in dictionary]
    #solution set consists of all the words that are in dictionary and matches the length
    self.solution=set() 
    self.N=len(grid)
    if self.N == 0 or len(self.grid[0]) == 0:     # handling situation when the input grid is empty
      self.visited = []
    else:
      self.visited=[[False for x in range(self.N)] for x in range(self.N)]     #keeping track of position already visited in grid
    #creating a new hashmap that creates a key of all prefixes and the entire word 
    self.word_map = {}
    #call the fucntion to populate the hashmap
    self.build_word_map(self.dictionary)

  def build_word_map(self, dictionary):
    #iterates through every word in dictionary
    for word in dictionary:
      #iterates through evry char in a word
      for i in range(1, len(word) + 1):
        prefix = word[:i]
        if prefix not in self.word_map:
          # adding prefix to hashmap and setting it to 0 indicating it is a prefix
          self.word_map[prefix] = 0
      # adding the entire word and setting it to 1 to indicate it is a complete word
      self.word_map[word] = 1
  
  def setGrid(self,grid):
    if not grid:
      return []
    self.N = len(grid)
    return [[letter.upper() for letter in row] for row in grid]
  
  def setDictionary(self,dictionary):
    #setting the dictionary
    self.dictionary=dictionary
  
  def setDictionary(self, dictionary):
    self.word_map = {} 
    self.build_word_map(dictionary)
  
  def is_valid(self, current_word):
    return len(current_word) >= 3 and self.word_map.get(current_word) == 1

  def getSolution(self):
    #handling situation when input dictionary is empty
    if not self.grid or not self.grid[0] or len(self.grid)!= len(self.grid[0]):
      return []
    if not self.dictionary: 
        return []
    #handling situation when input grid is empty
    if self.N == 0 or len(self.grid[0]) == 0:
      return []
    # going through each element in the grid and running a dfs on it
    for i in range(self.N):
      for j in range(self.N):
        if self.grid[i][j] == "Q" or self.grid[i][j] == "S":
          return []
        self.dfs(i,j,self.grid[i][j])
    print(f"This is the grid {self.grid}")
    print(f"This is the dictionary {self.dictionary}")
    return list(self.solution)
    
  
  def isvalid(self,current_word):
    # verifying if the word matches the condition to be added to the solution set
    return len(current_word)>=3 and current_word in self.dictionary

  def dfs(self,i,j,current_word):
    #making sure the loop is inside the grid and the xurrnet index hasnt been visited
    if i < 0 or i >= self.N or j < 0 or j >= self.N or self.visited[i][j]:
      return

    #if the prefix doesnt exist stop the dfs
    if current_word not in self.word_map:
      return
    #check if it is the valid word and the length is greater than or equal to 3
    if self.is_valid(current_word):
      self.solution.add(current_word)
    # marks the cell as visited
    self.visited[i][j] = True

    # move in all 8 directions to see if adding adjacent letters add to make the word
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for dr, dc in directions:
      #running dfs on new cells
      x = i + dr
      y = j + dc
      if 0 <= x < self.N and 0 <= y < self.N:
        self.dfs(x, y, current_word + self.grid[x][y])
      # try:
      #   self.dfs(x, y, current_word+self.grid[x][y])
      # except:
      #   continue
      
    #unmarks the visited cell
    self.visited[i][j] = False

def main():
    # grid = [["T", "W", "Y", "R"], 
    #         ["E", "N", "P", "H"], 
    #         ["G", "Z", "Qu", "R"], 
    #         ["O", "N", "T", "A"]]
    # dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", 
    #               "rat", "tar", "tarp", "ten", "went", "wet", "arty", "not", "quar"]
    # mygame = Boggle(grid, dictionary)
    # print(sorted(mygame.getSolution()))
    
    grid = [['A', 'B', 'C', 'J', 'K', 'S'], 
            ['D', 'E', 'F', 'M', 'N', 'O'], 
            ['G', 'H', 'I', 'P', 'Q', 'R'], 
            ['U', 'V', 'W', 'X', 'Y'], 
            ['E', 'I', 'N', 'O', 'U']]
    dictionary = ['EAB', 'EBC', 'JKS', 'DEF', 'PQR', 'SOR', 'ECB', 'EDB', 'EFB', 'EGH', 'EHI', 'EIH']
    mygame = Boggle(grid, dictionary)
    print(sorted(mygame.getSolution()))

if __name__ == "__main__":
    main()
