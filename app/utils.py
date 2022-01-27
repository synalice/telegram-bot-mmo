import asyncio
import functools
from concurrent.futures import ThreadPoolExecutor


__all__ = ["make_async"]


def make_async(executor=ThreadPoolExecutor(max_workers=32)):
	def decorator(function):
		@functools.wraps(function)
		async def wrapper(*args, **kwargs):
			loop = asyncio.get_running_loop()
			return await loop.run_in_executor(
				executor, functools.partial(function, **kwargs), *args
			)


		return wrapper


	return decorator
