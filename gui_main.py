import tkinter as tk
from tkinter import messagebox
import threading
import pandas as pd
import scapy.all as scapy
import os
import time

# Global variables
capturing = False
packets_list = []
log_file = "logs/captured_packets.xlsx"

# Ensure logs folder exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Function to capture packets
def capture_packets():
    global capturing, packets_list
    packets_list = []  # Reset packet list

    print("[INFO] Packet sniffing started...")
    
    while capturing:
        packet = scapy.sniff(count=1)  # Capture one packet at a time
        packets_list.append(packet[0])  # Save the packet
        print(f"[DEBUG] Captured: {packet[0].summary()}")  # Print captured packet

# Function to start sniffing
def start_sniffing():
    global capturing
    if capturing:
        messagebox.showinfo("Info", "Already Capturing!")
        return

    capturing = True
    threading.Thread(target=capture_packets, daemon=True).start()
    messagebox.showinfo("Success", "Packet Sniffing Started!")

# Function to stop sniffing and save logs
def stop_sniffing():
    global capturing, packets_list
    capturing = False
    time.sleep(1)  # Allow processing time

    print(f"[INFO] Packets Captured: {len(packets_list)}")  # Debugging print

    if packets_list:
        df = pd.DataFrame([{
            "Time": time.strftime("%Y-%m-%d %H:%M:%S"),
            "Packet Summary": pkt.summary()
        } for pkt in packets_list])

        try:
            df.to_excel(log_file, index=False, engine='openpyxl')
            messagebox.showinfo("Success", f"Logs Saved at {log_file}")
            print(f"[INFO] Log file saved at: {log_file}")

            # Automatically open the Excel file if created
            if os.path.exists(log_file):
                os.system(f'start excel "{log_file}"')  # For Windows
                # os.system(f'open "{log_file}"')  # For MacOS
                # os.system(f'xdg-open "{log_file}"')  # For Linux
        except Exception as e:
            print(f"[ERROR] Failed to save log file: {e}")
            messagebox.showerror("Error", "Failed to save log file!")
    else:
        print("[WARNING] No packets captured.")
        messagebox.showwarning("Warning", "No Packets Captured!")

# Function to exit
def exit_program():
    stop_sniffing()
    root.quit()

# GUI Setup
root = tk.Tk()
root.title("Intrusion Detection System")
root.geometry("400x300")
root.configure(bg="black")

# Labels
tk.Label(root, text="Intrusion Detection System", font=("Arial", 14, "bold"), fg="white", bg="black").pack(pady=10)
tk.Label(root, text="Network Traffic Monitor", font=("Arial", 10), fg="white", bg="black").pack(pady=5)

# Buttons
tk.Button(root, text="Start Sniffing", font=("Arial", 12), command=start_sniffing, bg="green", fg="white").pack(pady=10)
tk.Button(root, text="Stop Sniffing", font=("Arial", 12), command=stop_sniffing, bg="red", fg="white").pack(pady=10)
tk.Button(root, text="Exit", font=("Arial", 12), command=exit_program, bg="gray", fg="white").pack(pady=10)

# Run GUI
root.mainloop()
