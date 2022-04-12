
class WordWrap:
  def apply(self, expression, n_columns):
    if n_columns > len(expression):
      return expression

    while expression[0] == ' ':
      expression = expression[1:]

    parsedString = list(expression[:n_columns])
    i = n_columns - 1
    while i > 0:
      if parsedString[i] == ' ':
        j = i - 1
        while j > 0 and parsedString[j] == ' ':
          print(parsedString, j)
          parsedString = parsedString[:j]
          j -= 1
        parsedString[i] = '\n'
        remainder = ''.join(parsedString[i + 1:]) + expression[len(parsedString):]
        return ''.join(parsedString[:i + 1]) + \
            self.apply(remainder, n_columns)
      i -= 1

    remainder = expression[len(parsedString):]
    return ''.join(parsedString) + '\n' + self.apply(remainder, n_columns)
