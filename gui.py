import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('OurPasswords')

# header widget
header_label = ttk.Label(window, text='Our Passwords', font=('Times', 30, 'bold'))
header_label.pack()

# middle section
middle_frame = ttk.Frame(window)

# Password Table
middle_left = ttk.Frame(middle_frame)
table = ttk.Treeview(middle_left, columns=('site', 'username'), show='headings')
table.heading('site', text='Site')
table.heading('username', text='UserName')
middle_right = ttk.Frame(middle_frame)
middle_right_label = ttk.Label(middle_right, text='Text Label', background='yellow')
table.pack(side='left', expand=1, fill='both')
middle_right_label.pack(side='left', expand=1, fill='both')
middle_left.pack(side='left', expand=1, fill='both')
middle_right.pack(side='left', expand=1, fill='both')
middle_frame.pack(expand=1, fill='both')

# bottom section
bottom_frame = ttk.Frame(window)

# edit/save entries
bottom_left = ttk.Frame(bottom_frame)
site_name = tk.StringVar()
site_url = tk.StringVar()
user_name = tk.StringVar()
password = tk.StringVar()
site_name_label = ttk.Label(bottom_left, text='Site Name')
site_name_entry = ttk.Entry(bottom_left, textvariable=site_name)
site_url_label = ttk.Label(bottom_left, text='Url')
site_url_entry = ttk.Entry(bottom_left, textvariable=site_url)
user_name_label = ttk.Label(bottom_left, text='User Name')
user_name_entry = ttk.Entry(bottom_left, textvariable=user_name)
password_label = ttk.Label(bottom_left, text='Password')
password_entry = ttk.Entry(bottom_left, textvariable=password)

# Password generate
password_pick = tk.IntVar()
bottom_right = ttk.Frame(bottom_frame)
bottom_generate_label = ttk.Label(bottom_right, text='Password Generate', font=('Times', 15,))
bottom_rule1 = ttk.Separator(bottom_right, orient='horizontal')
bottom_rule2 = ttk.Separator(bottom_right, orient='horizontal')
bottom_radio_pick = ttk.Radiobutton(bottom_right, text='Pick for me', variable=password_pick, value=1)
bottom_radio_choose = ttk.Radiobutton(bottom_right, text='Use my own', variable=password_pick, value=0)
button_frame = ttk.Frame(bottom_right)
save_button = ttk.Button(button_frame, text='Save')
delete_button = ttk.Button(button_frame, text='Delete')

# save/edit layout
site_name_label.pack(fill='x', expand=1)
site_name_entry.pack(fill='x', expand=1)
site_url_label.pack(fill='x', expand=1)
site_url_entry.pack(fill='x', expand=1)
user_name_label.pack(fill='x', expand=1)
user_name_entry.pack(fill='x', expand=1)
password_label.pack(fill='x', expand=1)
password_entry.pack(fill='x', expand=1)
bottom_left.pack(side='left', expand=1, fill='both')

# Password Generate layout
bottom_generate_label.pack(expand=1, fill='x')
bottom_rule1.pack(expand=1, fill='x')
bottom_radio_pick.pack(expand=1, fill='x')
bottom_radio_choose.pack(expand=1, fill='x')
bottom_rule2.pack(expand=1, fill='x')
bottom_right.pack(side='left', expand=1, fill='both')
save_button.pack(side='left', expand=1, fill='both')
delete_button.pack(side='left', expand=1, fill='both')
button_frame.pack(expand=1, fill='both')

bottom_frame.pack(expand=1, fill='both')

window.mainloop()