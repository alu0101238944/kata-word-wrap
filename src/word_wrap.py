
class WordWrap:
  def apply(self, expression, n_columns):
    if n_columns > len(expression):
      return expression
    parsedString = list(expression[:n_columns])
    i = n_columns - 1
    while i > 0:
      if parsedString[i] == ' ':
        parsedString[i] = '\n'
        return ''.join(parsedString) + self.apply(expression[n_columns:], n_columns)
      i -= 1
    return ''.join(parsedString) + '\n' + self.apply(expression[n_columns:], n_columns)
