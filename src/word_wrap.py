
class WordWrap:
  def apply(self, expression, n_columns):
    return '\n'.join(expression.split(' '))
