import time

start=input("To start  press the Enter button")
start_time=time.time()
end=input("To end press the Enter button")
end_time=time.time()

elapsed_time=end_time-start_time
seconds=elapsed_time % 60
minutes=elapsed_time / 60

print(f"your elapsed time is {round(minutes,0)} min and {round(seconds,2)} seconds")
