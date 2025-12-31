Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tkinter as tk
>>> from tkinter import simpledialog
>>> class WBWData:
...     # Initial starting data
...     news_list = ["Welcome to the WBW Portal!", "Official Company News will appear here."]
...     comments_list = ["Cool logo!", "First comment!"]
...     likes = 0
...     dislikes = 0
...     has_voted = False
...     comments_enabled = True
... 
...     
>>> def refresh_news():
...     """Updates the news listbox display."""
...     news_display.delete(0, tk.END)
...     for post in reversed(WBWData.news_list):
...         news_display.insert(tk.END, f" > {post}")
... 
...         
>>> def refresh_comments():
...     """Updates the comments listbox and status label."""
...     comment_display.delete(0, tk.END)
...     if WBWData.comments_enabled:
...         lbl_comm_status.config(text="COMMENTS: ON", fg="green")
...         for c in reversed(WBWData.comments_list):
...             comment_display.insert(tk.END, f" 💬 {c}")
    else:
        lbl_comm_status.config(text="COMMENTS: OFF", fg="red")
        comment_display.insert(tk.END, " [Comments have been disabled by Admin]")

        
def handle_vote(vote_type):
    """Quietly updates votes and locks buttons."""
    if WBWData.has_voted:
        return 
    if vote_type == "like":
        WBWData.likes += 1
        lbl_likes.config(text=f"👍 {WBWData.likes}")
    else:
        WBWData.dislikes += 1
        lbl_dislikes.config(text=f"👎 {WBWData.dislikes}")
    
    WBWData.has_voted = True
    btn_lk.config(state="disabled")
    btn_dk.config(state="disabled")

    
def admin_login():
    """Access with password: jskhokhar28"""
    secret = simpledialog.askstring("WBW Admin", "Password:", show='*')
    if secret == "jskhokhar28":
        admin_panel.pack(pady=10)
        btn_login.pack_forget()

        
def exit_admin():
    """Closes Admin Panel and returns to user view."""
    admin_panel.pack_forget()
    btn_login.pack(side="bottom", pady=10)

    
def post_news():
    """Adds news story to the feed."""
    msg = entry_news.get()
    if msg:
        WBWData.news_list.append(msg)
        entry_news.delete(0, tk.END)
        refresh_news()

        
def post_user_comment():
    """Allows users to post comments if enabled."""
    if not WBWData.comments_enabled:
        return
    msg = entry_user_comment.get()
    if msg:
        WBWData.comments_list.append(msg)
        entry_user_comment.delete(0, tk.END)
        refresh_comments()

        
def toggle_comments():
    """Turns the comment section on or off."""
    WBWData.comments_enabled = not WBWData.comments_enabled
    refresh_comments()

    
def clear_all_comments():
    """Wipes the comment list completely."""
    WBWData.comments_list = []
    refresh_comments()

    
root = tk.Tk()
root.title("Wah Bai Wah Game Co.")
''
root.geometry("500x950")
''
root.configure(bg="white")
canvas = tk.Canvas(root, width=300, height=130, bg="white", highlightthickness=0)
canvas.pack(pady=10)
canvas.create_oval(10, 10, 290, 120, outline="blue", width=8)
1
canvas.create_text(150, 65, text="WBW", fill="blue", font=("Arial", 60, "bold italic"))
2
tk.Label(root, text="COMPANY NEWS", font=("Arial", 10, "bold"), bg="white", fg="blue").pack(pady=(10, 0))
frame_news = tk.Frame(root, bg="#f0f0f0", bd=2, relief="groove")
frame_news.pack(padx=30, pady=5, fill="both", expand=True)
news_display = tk.Listbox(frame_news, bg="white", font=("Arial", 11), borderwidth=0, highlightthickness=0)
news_display.pack(padx=5, pady=5, fill="both", expand=True)
lbl_comm_status = tk.Label(root, text="COMMENTS: ON", font=("Arial", 9, "bold"), bg="white")
lbl_comm_status.pack(pady=(10, 0))
frame_comm = tk.Frame(root, bg="#f0f0f0", bd=2, relief="groove")
frame_comm.pack(padx=30, pady=5, fill="both", expand=True)
comment_display = tk.Listbox(frame_comm, bg="white", font=("Arial", 10), borderwidth=0, highlightthickness=0)
comment_display.pack(padx=5, pady=5, fill="both", expand=True)
user_comm_frame = tk.Frame(root, bg="white")
user_comm_frame.pack(pady=5)
entry_user_comment = tk.Entry(user_comm_frame, width=30)
entry_user_comment.pack(side="left", padx=5)
tk.Button(user_comm_frame, text="Post Comment", command=post_user_comment).pack(side="left")
frame_social = tk.Frame(root, bg="white")
frame_social.pack(pady=10)
btn_lk = tk.Button(frame_social, text="LIKE", bg="#e1f5fe", width=8, command=lambda: handle_vote("like"))
btn_lk.grid(row=0, column=0, padx=10)
lbl_likes = tk.Label(frame_social, text="👍 0", bg="white", font=("Arial", 9, "bold"))
lbl_likes.grid(row=1, column=0)
btn_dk = tk.Button(frame_social, text="DISLIKE", bg="#ffebee", width=8, command=lambda: handle_vote("dislike"))
btn_dk.grid(row=0, column=1, padx=10)
lbl_dislikes = tk.Label(frame_social, text="👎 0", bg="white", font=("Arial", 9, "bold"))
lbl_dislikes.grid(row=1, column=1)
admin_panel = tk.Frame(root, bg="#e3f2fd", padx=10, pady=10, bd=1, relief="solid")
tk.Label(admin_panel, text="--- ADMIN CONTROLS ---", bg="#e3f2fd", font=("Arial", 8, "bold")).pack()
entry_news = tk.Entry(admin_panel, width=40)
entry_news.pack(pady=5)
tk.Button(admin_panel, text="PUBLISH NEWS STORY", bg="blue", fg="white", command=post_news).pack(pady=2)
tk.Button(admin_panel, text="TOGGLE COMMENTS ON/OFF", bg="orange", command=toggle_comments).pack(pady=2)
tk.Button(admin_panel, text="CLEAR ALL COMMENTS", bg="black", fg="white", command=clear_all_comments).pack(pady=2)
tk.Button(admin_panel, text="EXIT ADMIN MODE", bg="red", fg="white", command=exit_admin).pack(pady=5)
btn_login = tk.Button(root, text="[ Admin Login ]", fg="#ddd", bg="white", bd=0, command=admin_login)
btn_login.pack(side="bottom", pady=10)
refresh_news()
refresh_comments()
root.mainloop()
