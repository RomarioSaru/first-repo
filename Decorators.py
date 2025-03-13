import time

def a_decorator(some_func):
	def wrapper_name(*args, **kwargs):
		start = time.time()
		result = some_func(*args, **kwargs)
		end = time.time()
		print(f"The function {some_func.__name__} took {(end-start)*1000} ms to finish")
		return result
	return wrapper_name


@a_decorator
def return_sum(numbers):
	summ = 0
	for i in numbers:
		summ += i
	return summ

@a_decorator
def return_prod(numbers):
	prod = 1
	for i in numbers:
		prod *= i
	return prod

lst = [1, 2, 3, 4]
print(return_sum(lst))
print(return_prod(lst))

print("test print to be deleted")