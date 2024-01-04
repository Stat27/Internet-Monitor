import psutil
import tkinter as tk
import datetime
import GPUtil

class NetworkMonitor:
    def __init__(self):
        # Initialize the main window
        self.main_window = tk.Tk()
        self.main_window.title('Network Monitor')
        self.main_window.geometry('400x550')

        self.create_labels()
        self.refresh_labels()

    def create_labels(self):
        # Header label for the application
        header_label = tk.Label(self.main_window, text='Network Monitor', font=('Helvetica', 20), fg='blue', pady=10)
        header_label.pack()

        # Frame to organize the labels
        self.info_frame = tk.Frame(self.main_window)
        self.info_frame.pack(pady=20)

        self.label_time = tk.Label(self.info_frame, font=('Helvetica', 14), fg='blue')
        self.label_time.pack(pady=5)

        self.label_cpu = tk.Label(self.info_frame, font=('Helvetica', 14), fg='green')
        self.label_cpu.pack(pady=5)

        self.label_gpu = tk.Label(self.info_frame, font=('Helvetica', 14), fg='green')
        self.label_gpu.pack(pady=5)

        self.label_memory = tk.Label(self.info_frame, font=('Helvetica', 14), fg='green')
        self.label_memory.pack(pady=5)

        self.label_disk = tk.Label(self.info_frame, font=('Helvetica', 14), fg='green')
        self.label_disk.pack(pady=5)

        self.label_disk_total = tk.Label(self.info_frame, font=('Helvetica', 14), fg='green')
        self.label_disk_total.pack(pady=5)

        self.label_disk_free = tk.Label(self.info_frame, font=('Helvetica', 14), fg='green')
        self.label_disk_free.pack(pady=5)

        self.label_disk_used = tk.Label(self.info_frame, font=('Helvetica', 14), fg='green')
        self.label_disk_used.pack(pady=5)

        self.label_data_recv = tk.Label(self.info_frame, font=('Helvetica', 14), fg='green')
        self.label_data_recv.pack(pady=5)

        self.label_data_sent = tk.Label(self.info_frame, font=('Helvetica', 14), fg='green')
        self.label_data_sent.pack(pady=5)

    def get_gpu_usage(self):
        # Get GPU usage if GPU is available, otherwise return 'N/A'
        gpus = GPUtil.getGPUs()
        
        
        if gpus:
            return f'{gpus[0].load * 100:.1f}%' 
        else:
            return 'N/A'

    def refresh_labels(self):
        
        # Fetch and update system information
        disk_usage = psutil.disk_usage('/')
        memory_usage = psutil.virtual_memory()
        cpu_usage = psutil.cpu_percent(interval=1)
        net_info = psutil.net_io_counters()

        self.label_time.config(text=f'Current Time: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        
        self.label_cpu.config(text=f'CPU Usage: {cpu_usage}%')
        
        self.label_gpu.config(text=f'GPU Usage: {self.get_gpu_usage()}')
        
        self.label_memory.config(text=f'Memory Usage: {memory_usage.percent}%')
        
        self.label_disk.config(text=f'Disk Usage: {disk_usage.percent}%')
        
        self.label_disk_total.config(text=f'Total Disk Space: {disk_usage.total / 1024 ** 3:.2f}GB')
        
        self.label_disk_free.config(text=f'Free Disk Space: {disk_usage.free / 1024 ** 3:.2f}GB')
        
        self.label_disk_used.config(text=f'Used Disk Space: {disk_usage.used / 1024 ** 3:.2f}GB')
        
        self.label_data_recv.config(text=f'Data Received: {net_info.bytes_recv / 1024 ** 2:.2f}MB')
        
        self.label_data_sent.config(text=f'Data Sent: {net_info.bytes_sent / 1024 ** 2:.2f}MB')

        self.main_window.after(500, self.refresh_labels)

    def run(self):
        
        self.main_window.mainloop()

if __name__ == "__main__":
    # Create and run the network monitor
    network_monitor = NetworkMonitor()
    network_monitor.run()
