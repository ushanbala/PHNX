import tkinter.messagebox

def alert(title,message,msg_type):
    if msg_type=='info':
        # To show an information dialog
        tkinter.messagebox.showinfo(title=title, message=message)
    elif msg_type=='warn':
        # To show a warning dialog
        tkinter.messagebox.showwarning(title=title, message=message)
    elif msg_type=='error':
        # To show an error dialog
        tkinter.messagebox.showerror(title=title, message=message)
    else:
        print(f"No alert type called: {msg_type}")

