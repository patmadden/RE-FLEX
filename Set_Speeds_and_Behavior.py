import tkinter as tk
import os

def update_values():
    global timehigh, timelow, rapidvalue, rapidtimehigh, rapidtimelow, ratelimitsleep

    timehigh = float(timehigh_entry.get())
    timelow = float(timelow_entry.get())
    rapidvalue = int(rapidvalue_entry.get())
    rapidtimehigh = float(rapidtimehigh_entry.get())
    rapidtimelow = float(rapidtimelow_entry.get())
    ratelimitsleep = int(ratelimitsleep_entry.get())

    with open("userdata/speed_behavior_values.py", "w") as f:
        f.write(f"timehigh={timehigh}\n")
        f.write(f"timelow={timelow}\n")
        f.write(f"rapidvalue={rapidvalue}\n")
        f.write(f"rapidtimehigh={rapidtimehigh}\n")
        f.write(f"rapidtimelow={rapidtimelow}\n")
        f.write(f"ratelimitsleep={ratelimitsleep}\n")
    print("Speeds and Behavior set")

root = tk.Tk()
root.title("Set Values")

if os.path.exists("userdata/speed_behavior_values.py"):

    import userdata.speed_behavior_values as sbv
    timehigh_label = tk.Label(root, text="timehigh")
    timehigh_label.grid(row=0, column=0)

    timehigh_entry = tk.Entry(root)
    timehigh_entry.insert(0, sbv.timehigh)
    timehigh_entry.grid(row=0, column=1)

    timelow_label = tk.Label(root, text="timelow")
    timelow_label.grid(row=1, column=0)

    timelow_entry = tk.Entry(root)
    timelow_entry.insert(0, sbv.timelow)
    timelow_entry.grid(row=1, column=1)

    rapidvalue_label = tk.Label(root, text="rapidvalue")
    rapidvalue_label.grid(row=2, column=0)

    rapidvalue_entry = tk.Entry(root)
    rapidvalue_entry.insert(0, sbv.rapidvalue)
    rapidvalue_entry.grid(row=2, column=1)

    rapidtimehigh_label = tk.Label(root, text="rapidtimehigh")
    rapidtimehigh_label.grid(row=3, column=0)

    rapidtimehigh_entry = tk.Entry(root)
    rapidtimehigh_entry.insert(0, sbv.rapidtimehigh)
    rapidtimehigh_entry.grid(row=3, column=1)

    rapidtimelow_label = tk.Label(root, text="rapidtimelow")
    rapidtimelow_label.grid(row=4, column=0)

    rapidtimelow_entry = tk.Entry(root)
    rapidtimelow_entry.insert(0, sbv.rapidtimelow)
    rapidtimelow_entry.grid(row=4, column=1)

    ratelimitsleep_label = tk.Label(root, text="ratelimitsleep")
    ratelimitsleep_label.grid(row=5, column=0)

    ratelimitsleep_entry = tk.Entry(root)
    ratelimitsleep_entry.insert(0, sbv.ratelimitsleep)
    ratelimitsleep_entry.grid(row=5, column=1)

else:
    timehigh_label = tk.Label(root, text="timehigh")
    timehigh_label.grid(row=0, column=0)

    timehigh_entry = tk.Entry(root)
    timehigh_entry.insert(0, "2.8")
    timehigh_entry.grid(row=0, column=1)

    timelow_label = tk.Label(root, text="timelow")
    timelow_label.grid(row=1, column=0)

    timelow_entry = tk.Entry(root)
    timelow_entry.insert(0, "2.2")
    timelow_entry.grid(row=1, column=1)

    rapidvalue_label = tk.Label(root, text="rapidvalue")
    rapidvalue_label.grid(row=2, column=0)

    rapidvalue_entry = tk.Entry(root)
    rapidvalue_entry.insert(0, "150")
    rapidvalue_entry.grid(row=2, column=1)

    rapidtimehigh_label = tk.Label(root, text="rapidtimehigh")
    rapidtimehigh_label.grid(row=3, column=0)

    rapidtimehigh_entry = tk.Entry(root)
    rapidtimehigh_entry.insert(0, "0.4")
    rapidtimehigh_entry.grid(row=3, column=1)

    rapidtimelow_label = tk.Label(root, text="rapidtimelow")
    rapidtimelow_label.grid(row=4, column=0)

    rapidtimelow_entry = tk.Entry(root)
    rapidtimelow_entry.insert(0, "0.2")
    rapidtimelow_entry.grid(row=4, column=1)

    ratelimitsleep_label = tk.Label(root, text="ratelimitsleep")
    ratelimitsleep_label.grid(row=5, column=0)

    ratelimitsleep_entry = tk.Entry(root)
    ratelimitsleep_entry.insert(0, "45")
    ratelimitsleep_entry.grid(row=5, column=1)

update_button = tk.Button(root, text="Update", command=update_values)
update_button.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
