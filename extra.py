import time

start=time.perf_counter()
print(sum(range(1000)))
end=time.perf_counter()

print(f"Time taken: {end-start:.6f} seconds")