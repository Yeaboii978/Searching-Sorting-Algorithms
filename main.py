import bubble, linear, binary, merge, insertion

search_mode = input("Linear or Bubble or Binary or Merge or Inserion: ").lower()

if search_mode == "linear":
  linear.linear()
elif search_mode == "bubble":
  bubble.bubble()
elif search_mode == "binary":
  binary.binary()
elif search_mode == "merge":
  merge.merge()
elif search_mode == "insertion":
  insertion.insertion()
