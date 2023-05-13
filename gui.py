import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x525')
window.title('OurPasswords')
window.minsize(width=525, height=600)
# header section
card_search = tk.StringVar()
header_label = ttk.Label(window, text='Our Passwords', font=('Times', 30, 'bold'))
search_frame = ttk.Frame(window)
card_search_label = ttk.Label(search_frame, text='Search Entries', font=('Times', 15,))
card_search_entry = ttk.Entry(search_frame, textvariable=card_search, width=20)

# middle section
middle_frame = ttk.Frame(window)

# Password Table
middle_left = ttk.Frame(middle_frame)
table = ttk.Treeview(middle_left, columns=('site', 'username', 'action'), show='headings')
action_frame = ttk.Frame(table)
action_button = ttk.Button(action_frame, text="Web")
table.heading('site', text='Site')
table.heading('username', text='UserName')

# card section
middle_right = ttk.Frame(middle_frame)
card_site = tk.StringVar()
card_user = tk.StringVar()
card_search_sep = ttk.Separator(middle_right)
card_site_label = ttk.Label(middle_right, text='Site')
card_site_entry = ttk.Entry(middle_right, textvariable=card_site)
card_user_label = ttk.Label(middle_right, text='UserName')
card_user_entry = ttk.Entry(middle_right, textvariable=card_user)

# bottom section
bottom_frame = ttk.Frame(window)

# edit/save entries
bottom_left = ttk.Frame(bottom_frame)
bottom_edit_label = ttk.Label(bottom_left, text='Add/Edit Entry', font=('Times', 15,))
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
delete_button = ttk.Button(button_frame, text='Delete/Cancel')


# <editor-fold desc="Master Layout">
# table layout
table.pack(side='left', expand=1, fill='y')
middle_left.pack(side='left', expand=1, fill='y', padx=10)

# result layout
# card_search_sep.pack(expand=1, fill='x')
# card_site_label.pack(expand=1, fill='x')
# card_site_entry.pack(expand=1, fill='x')
# card_user_label.pack(expand=1, fill='x')
# card_user_entry.pack(expand=1, fill='x')
# middle_right.pack(side='left', expand=1, fill='both', padx=10)

# save/edit layout
bottom_edit_label.pack(fill='x', expand=1)
site_name_label.pack(fill='x', expand=1)
site_name_entry.pack(fill='x', expand=1)
site_url_label.pack(fill='x', expand=1)
site_url_entry.pack(fill='x', expand=1)
user_name_label.pack(fill='x', expand=1)
user_name_entry.pack(fill='x', expand=1)
password_label.pack(fill='x', expand=1)
password_entry.pack(fill='x', expand=1)
bottom_left.pack(side='left', expand=1, fill='both', padx=10, pady=10)
# Password Generate layout
bottom_generate_label.pack(expand=1, fill='x')
bottom_rule1.pack(expand=1, fill='x')
bottom_radio_pick.pack(expand=1, fill='x')
bottom_radio_choose.pack(expand=1, fill='x')
bottom_rule2.pack(expand=1, fill='x')
save_button.pack(side='left', expand=1, fill='both')
delete_button.pack(side='left', expand=1, fill='both')
button_frame.pack(expand=1, fill='both')

bottom_right.pack(side='left', expand=1, fill='both', pady=10, padx=10)

# frame layouts
middle_frame.pack(expand=1, fill='both')
bottom_frame.pack(expand=1, fill='both')
# </editor-fold>

window.mainloop()
