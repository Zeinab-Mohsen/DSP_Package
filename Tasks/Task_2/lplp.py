import tkinter as tk

def modify_variable():
    global my_variable
    my_variable = 20

# Create the main window
root = tk.Tk()

# Create a button that calls the modify_variable function
button = tk.Button(root, text="Modify Variable", command=modify_variable)
button.pack()

# Initialize the variable
my_variable = 10

# Start the GUI event loop
print(my_variable)
root.mainloop()
print(my_variable)

# Now, my_variable will be updated when the button is clicked
