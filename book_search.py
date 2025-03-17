import tkinter as tk
from tkinter import messagebox
import webbrowser
from googlesearch import search

def search_book():
    book_name = entry.get()
    if not book_name:
        messagebox.showwarning("Input Error", "Please enter a book name.")
        return
    
    query = f"{book_name} read online"
    results = list(search(query, num_results=5))
    
    if results:
        read_online_button.config(state=tk.NORMAL, command=lambda: webbrowser.open(results[0]))
        download_button.config(state=tk.NORMAL, command=lambda: download_book(book_name))
    else:
        messagebox.showinfo("Not Found", "Book not available online.")
        read_online_button.config(state=tk.DISABLED)
        download_button.config(state=tk.DISABLED)

def download_book(book_name):
    query = f"{book_name} pdf download"
    results = list(search(query, num_results=5))
    
    if results:
        webbrowser.open(results[0])
    else:
        messagebox.showinfo("Not Found", "PDF version not available.")

# GUI Setup
root = tk.Tk()
root.title("Book Search")
root.geometry("400x300")

tk.Label(root, text="Enter Book Name:").pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Search", command=search_book).pack(pady=10)

read_online_button = tk.Button(root, text="Read Online", state=tk.DISABLED)
download_button = tk.Button(root, text="Download PDF", state=tk.DISABLED)

read_online_button.pack(pady=5)
download_button.pack(pady=5)

root.mainloop()

