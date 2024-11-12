import tkinter as tk
from tkinter import messagebox


def submit_review():
    rating = review_var.get()
    if rating == 0:
        messagebox.showwarning("Review", "Please select a rating!")
    else:
        messagebox.showinfo(
            "Review", f"Thanks for your review! You rated {rating} stars.")


root = tk.Tk()
root.title("Football Scores and Reviews")
root.geometry("400x500")
root.config(bg="#1e1e1e")


header_label = tk.Label(root, text="Football Game Scores", font=("Helvetica", 18, "bold"),
                        bg="#1e1e1e", fg="white")
header_label.pack(pady=20)


scores = [
    "Team A 2 - 1 Team B",
    "Team C 3 - 3 Team D",
    "Team E 1 - 0 Team F",
    "Team G 2 - 2 Team H",
    "Team I 0 - 4 Team J"
]
score_labels = []
for score in scores:
    score_label = tk.Label(root, text=score, font=(
        "Helvetica", 14), bg="#1e1e1e", fg="white")
    score_label.pack(pady=5)
    score_labels.append(score_label)


spacer_label = tk.Label(root, bg="#1e1e1e", height=2)
spacer_label.pack(pady=20)


review_frame = tk.Frame(root, bg="#1e1e1e")
review_frame.pack(pady=20)


review_label = tk.Label(review_frame, text="Rate this interface (1 to 5 stars):", font=("Helvetica", 12),
                        bg="#1e1e1e", fg="white")
review_label.grid(row=0, column=0, columnspan=5, pady=5)


review_var = tk.IntVar()


stars = []
for i in range(5):
    star_button = tk.Radiobutton(review_frame, text="★", font=("Helvetica", 20), bg="#1e1e1e",
                                 fg="gold", activebackground="#1e1e1e", activeforeground="gold",
                                 variable=review_var, value=i+1, selectcolor="#2c2f38", indicatoron=0)
    star_button.grid(row=1, column=i, padx=5)


submit_button = tk.Button(root, text="Submit Review", font=("Helvetica", 12),
                          command=submit_review, bg="#1e1e1e", fg="white")
submit_button.pack(pady=10)


root.mainloop()
