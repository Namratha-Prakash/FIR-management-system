import tkinter as tk
from tkinter import ttk

def display_fir_records():
    # Read the records from the victim.txt file
    with open("victim.txt", "r") as file:
        records = file.readlines()
    
    # Create a Tkinter window
    window = tk.Tk()
    window.title("FIR Records")
    window.configure(bg="#b1dee3")  # Set background color
    
    # Create a Treeview widget
    treeview = ttk.Treeview(window)
    treeview["columns"] = ("FIR No.", "Victim Name", "Accused Name", "Case Date", "Case Time", "Case Details", "Case Status")
    treeview.heading("#0", text="Record")
    treeview.column("#0", width=70, stretch=tk.NO)
    
    # Define column alignment
    alignments = ("center", "center", "center", "center", "center", "center", "center")
    
    for column, alignment in zip(treeview["columns"], alignments):
        treeview.heading(column, text=column)
        treeview.column(column, width=150, anchor=alignment)
    
    # Insert the records into the Treeview
    for i, record in enumerate(records, start=1):
        record = record.strip().split("|")
        fir_no = record[0]
        victim_name = record[1]
        accused_name = record[2]
        case_date = record[3]
        case_time = record[4]
        case_details = record[5]
        case_status = record[6]
        
        treeview.insert("", "end", text=str(i), values=(fir_no, victim_name, accused_name, case_date, case_time, case_details, case_status))
    
    # Pack the Treeview widget
    treeview.pack(padx=10, pady=10)
    
    # Start the Tkinter event loop
    window.mainloop()

# Call the display_fir_records function to display the records
display_fir_records()
