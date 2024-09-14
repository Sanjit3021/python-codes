def greet(fx):
  """Decorates a function to add a greeting and closing message."""
  def mfx():
    """Inner function that executes the decorated function."""
    print("Good Morning")
    fx()
    print("Thanks for using this function")
    return mfx
  return mfx

@greet
def hello():
  """Prints 'Hello World'."""
  print("Hello World")

def add(a, b):
  """Prints the sum of a and b."""
  print(a + b)

# Call the decorated hello function
hello()

# Call the add function (not decorated)
add(5, 3)