from time import perf_counter

def timer(func):
  def wrapper(*args, **kwargs):
    start = perf_counter()
    result = func(*args, **kwargs)
    end = perf_counter()
    print(f"{func.__name__} took {1000*(end-start):.4f}ms")
    return result
  return wrapper