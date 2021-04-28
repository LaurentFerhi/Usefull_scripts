# Transform merged excel
Read xlsx files with merged data and import it to a DataFrame with unmerged cells
    A   B  
  +---+---+
1 | a | 0 |
  |   | 1 |
  |   | 2 |
  +---+---+
2 | b | 3 |
  +---+---+

Becomes the following dataframe:
  
    A   B  
  +---+---+
1 | a | 0 |
  +---+---+
2 | a | 1 |
  +---+---+
3 | a | 2 |
  +---+---+
4 | b | 3 |
  +---+---+
