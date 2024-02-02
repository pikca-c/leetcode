  def lengthOfLastWord(self, s):
      words = s.strip().split(" ")
      word = words[len(words)-1]
      return len(word)
