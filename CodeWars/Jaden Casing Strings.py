def toJadenCase(string):
  return " ".join(w.capitalize() for w in string.split())

x = toJadenCase("How can mirrors be real if our eyes aren't real")
print(x)