import time
import keyboard

def time_tracking_game():
    print("==================================================")
    print("Time Tracking Challenge!")
    print("Instructions: Try to press SPACEBAR exactly 5 seconds after starting.")
    print("==================================================")
    
    input("Press ENTER when you are ready to start the clock...")
    print("\nClock started! Count to 5 seconds and hit SPACEBAR...")
    
    # Step 2: Initialize the anchor time
    start_time = time.time()
    
    # Step 4: Wait and listen specifically for the spacebar
    keyboard.wait('space')
    
    # Step 5: Capture the finish time immediately
    end_time = time.time()
    
    # Step 6: Do the math (Seconds to Milliseconds)
    total_elapsed_seconds = end_time - start_time
    total_elapsed_ms = total_elapsed_seconds * 1.000
    
    # Step 7: Calculate the accuracy
    target_ms = 5.000
    difference_ms = total_elapsed_ms - target_ms
    
    print("\n--------------------------------------------------")
    print(f"Total time since initialization: {total_elapsed_ms:.2f} s")
    
    if abs(difference_ms) < 0.500:
        print(f"Incredible! You were off by only {difference_ms:.2f} s! You are a poor man pikin.")
    elif difference_ms < 0.00:
        print(f"A bit too fast! You pressed it {abs(difference_ms):.2f} s early. You are somewhat of a failure.")
    elif difference_ms > 1.00:
        print(f"You pressed it {difference_ms:.2f} s late. You no get hope")
    else:
        print(f"A bit too slow! You pressed it {difference_ms:.2f} s late. You are a failure.")
    print("--------------------------------------------------")

if __name__ == "__main__":
    time_tracking_game()