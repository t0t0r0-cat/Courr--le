import tkinter as tk
from tkinter import ttk
from tkinterweb import HtmlFrame


def update_button_states(*args):
    """
    Enable the buttons only when the URL field is not empty.
    """
    has_url = bool(url_var.get().strip())

    if has_url:
        text_button.state(["!disabled"])
        element_button.state(["!disabled"])
    else:
        text_button.state(["disabled"])
        element_button.state(["disabled"])


def on_text_button_click():
    text_content = text_entry.get("1.0", tk.END).strip()
    url = url_var.get().strip()

    if not text_content:
        status_label.config(text="Veuillez entrer du texte.")
        return

    status_label.config(
        text=f"Texte ajouté vers {url}"
    )


def on_submit():
    btn.state(["disabled"])
    btn.config(text="Travail…")

    def done():
        btn.config(text="Nouveau élément texte")
        btn.state(["!disabled"])

    root.after(2000, done)


# Main window
root = tk.Tk()
root.title("Créer un Courr-Île : Mode Facile")
root.geometry("1000x600")
root.minsize(700, 400)
root.resizable(True, True)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Resizable horizontal splitter
panes = ttk.PanedWindow(root, orient=tk.HORIZONTAL)
panes.grid(row=0, column=0, sticky="nsew")

# ============================================================
# Left pane
# ============================================================

left_frame = ttk.Frame(panes, padding=20)
left_frame.columnconfigure(0, weight=1)
left_frame.rowconfigure(0, weight=1)

# This frame remains centered inside the left pane
controls_frame = ttk.Frame(left_frame)
controls_frame.grid(row=0, column=0)

controls_frame.columnconfigure(1, weight=1)

# Title
ttk.Label(
    controls_frame,
    text="Messages",
    font=("Segoe UI", 16, "bold")
).grid(
    row=0,
    column=0,
    columnspan=2,
    pady=(0, 25)
)

# URL field
ttk.Label(
    controls_frame,
    text="URL du bouton"
).grid(
    row=1,
    column=0,
    sticky="e",
    padx=(0, 10),
    pady=6
)

url_var = tk.StringVar()

url_entry = ttk.Entry(
    controls_frame,
    textvariable=url_var,
    width=35
)
url_entry.grid(
    row=1,
    column=1,
    pady=6
)

# Text field
ttk.Label(
    controls_frame,
    text="Texte à ajouter"
).grid(
    row=2,
    column=0,
    sticky="ne",
    padx=(0, 10),
    pady=6
)

text_entry = tk.Text(
    controls_frame,
    width=35,
    height=5,
    wrap="word"
)
text_entry.grid(
    row=2,
    column=1,
    pady=6
)

# Button for adding text
text_button = ttk.Button(
    controls_frame,
    text="Nouvelle boîte de texte",
    command=on_text_button_click
)
text_button.grid(
    row=3,
    column=0,
    columnspan=2,
    pady=8
)

# Loading-state button
btn = ttk.Button(
    controls_frame,
    text="Nouveau élément texte",
    command=on_submit
)
btn.grid(
    row=4,
    column=0,
    columnspan=2,
    pady=8
)

# Another button
element_button = ttk.Button(
    controls_frame,
    text="Nouvelle boîte de texte avec bouton"
)
element_button.grid(
    row=5,
    column=0,
    columnspan=2,
    pady=8
)

# Status label
status_label = ttk.Label(
    controls_frame,
    text=""
)
status_label.grid(
    row=6,
    column=0,
    columnspan=2,
    pady=10
)

# Update button states whenever the URL changes
url_var.trace_add("write", update_button_states)

# Disable URL-dependent buttons initially
text_button.state(["disabled"])
element_button.state(["disabled"])

# ============================================================
# Right pane: HTML preview
# ============================================================

right_frame = ttk.Frame(panes, padding=10)
right_frame.rowconfigure(0, weight=1)
right_frame.columnconfigure(0, weight=1)

html_view = HtmlFrame(right_frame)
html_view.grid(
    row=0,
    column=0,
    sticky="nsew"
)

html_view.load_html("""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial;
            padding: 20px;
            background: #f5f5f5;
        }

        h1 {
            color: #3366cc;
        }

        .card {
            background: white;
            padding: 20px;
            border-radius: 8px;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Prévisualisation</h1>
        <p>Le contenu HTML apparaîtra ici.</p>
    </div>
</body>
</html>
""")

# ttk.PanedWindow does not support minsize
panes.add(left_frame, weight=1)
panes.add(right_frame, weight=1)

root.mainloop()
