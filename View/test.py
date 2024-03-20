import tkinter as tk

def search():
    query = entry.get()
    # Perform search action here
    print("Searching for:", query)

root = tk.Tk()
root.title("Search Bar Inside Navbar")

# Create a frame for the navigation bar
navbar_frame = tk.Frame(root, bg="blue")
navbar_frame.pack(side="top", fill="x")

# Create the search entry inside the navbar
entry = tk.Entry(navbar_frame, width=30)
entry.pack(side="left", padx=10, pady=10)

# Create the search button inside the navbar
search_button = tk.Button(navbar_frame, text="Search", command=search)
search_button.pack(side="left", padx=10, pady=10)

root.mainloop()
