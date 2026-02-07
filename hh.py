workers = []

workers.append(("Stacey", "worker", 2))
workers.append(("Jesika", "agent", 4))
workers.append(("Matthew", "officer", 6))

print(f"all workers: {workers}")
print(f"first worker: ", {workers[0]})
print(f"second worker: ", {workers[1]})
print(f"third worker: ", {workers[2]})

min_experience = 100
youngest_worker = None

for worker in workers:
    name, position, experience = worker
    if experience < min_experience:
        min_experience = experience
        youngest_worker = worker

print(f"{youngest_worker}")

