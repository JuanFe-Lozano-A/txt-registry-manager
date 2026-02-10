import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import time
from .styles import *
from .manager import CompanyManager

# =============================================================================
# GRAPHICAL INTERFACE - SPLASH SCREEN
# =============================================================================

class ModernSplash(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Loading...")
        self.overrideredirect(True) 
        
        w, h = 500, 300
        ws, hs = self.winfo_screenwidth(), self.winfo_screenheight()
        x, y = (ws//2) - (w//2), (hs//2) - (h//2)
        self.geometry(f"{w}x{h}+{x}+{y}")
        self.configure(bg=COLOR_PRIMARY)
        
        self.canvas = tk.Canvas(self, width=w, height=h, bg=COLOR_PRIMARY, highlightthickness=0)
        self.canvas.pack()
        
        self.canvas.create_text(w//2, h//2 - 40, text="Business Management v2.0", fill="white", font=("Segoe UI", 20, "bold"))
        self.canvas.create_text(w//2, h//2 - 10, text="Initializing components...", fill="#bdc3c7", font=("Segoe UI", 10))
        
        self.angle = 0
        self.running = True
        self.parent = parent
        self.animate()
        
    def animate(self):
        if not self.running: return
        self.canvas.delete("arc")
        x_center, y_center = 250, 200
        radius = 30
        self.canvas.create_arc(
            x_center - radius, y_center - radius,
            x_center + radius, y_center + radius,
            start=self.angle, extent=120, style="arc", width=4, outline=COLOR_ACCENT, tags="arc"
        )
        self.angle = (self.angle - 10) % 360
        self.after(20, self.animate)

    def finish(self):
        self.running = False
        time.sleep(0.5)
        self.destroy()
        self.parent.deiconify()

# =============================================================================
# GRAPHICAL INTERFACE - MAIN WINDOW
# =============================================================================

class CompanyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw() 
        self.manager = CompanyManager()

        self.title("Business Management System")
        self.geometry("1000x700")
        self.minsize(900, 600)
        self.configure(bg=COLOR_BG)

        self.setup_styles()
        self.create_interface()

        self.splash = ModernSplash(self)
        self.after(3000, self.splash.finish)

    def setup_styles(self):
        style = ttk.Style(self)
        style.theme_use('clam')
        style.configure("TFrame", background=COLOR_BG)
        style.configure("White.TFrame", background=COLOR_WHITE)
        style.configure("Card.TFrame", background=COLOR_WHITE, relief="flat")
        style.configure("TLabel", background=COLOR_WHITE, foreground=COLOR_TEXT, font=FONT_NORMAL)
        style.configure("Header.TLabel", background=COLOR_PRIMARY, foreground="white", font=FONT_TITLE)
        style.configure("Subtitle.TLabel", background=COLOR_WHITE, foreground=COLOR_PRIMARY, font=FONT_SUBTITLE)
        style.configure("TEntry", fieldbackground="#fdfdfd", padding=5, relief="flat", borderwidth=1)
        style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=8)
        style.configure("Accent.TButton", background=COLOR_ACCENT, foreground="white")
        style.configure("Danger.TButton", background=COLOR_DANGER, foreground="white")
        
        style.configure("Treeview", font=FONT_NORMAL, rowheight=30)
        style.map("Treeview", background=[("selected", COLOR_ACCENT)])

    def create_interface(self):
        header_frame = tk.Frame(self, bg=COLOR_PRIMARY, height=80)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        header_frame.pack_propagate(False)
        tk.Label(header_frame, text="🏢 Company Management System", font=("Segoe UI", 22, "bold"), bg=COLOR_PRIMARY, fg="white").pack(pady=20, padx=20, anchor="w")

        self.create_menu()
        content_frame = ttk.Frame(self)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Form
        card_form = ttk.Frame(content_frame, style="Card.TFrame", padding=20)
        card_form.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 20))
        ttk.Label(card_form, text="📝 Company Data", style="Subtitle.TLabel").pack(anchor="w", pady=(0, 15))

        self.create_input(card_form, "NIT / ID:", "entr_nit")
        self.create_input(card_form, "Company Name:", "entr_name")
        self.create_input(card_form, "Physical Address:", "entr_address")
        self.create_input(card_form, "Annual Budget ($):", "entr_budget")

        btn_frame = ttk.Frame(card_form, style="White.TFrame")
        btn_frame.pack(fill=tk.X, pady=20)
        ttk.Button(btn_frame, text="💾 Save Changes", style="Accent.TButton", command=self.save_company).pack(fill=tk.X, pady=5)
        ttk.Button(btn_frame, text="🧹 Clear", command=self.clear_form).pack(fill=tk.X, pady=5)
        ttk.Button(btn_frame, text="🗑️ Delete", style="Danger.TButton", command=self.delete_selected).pack(fill=tk.X, pady=5)

        # Table
        card_list = ttk.Frame(content_frame, style="Card.TFrame", padding=20)
        card_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        search_frame = ttk.Frame(card_list, style="White.TFrame")
        search_frame.pack(fill=tk.X, pady=(0, 10))
        self.entr_search = ttk.Entry(search_frame)
        self.entr_search.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.entr_search.bind("<KeyRelease>", self.filter_list)

        cols = ("nit", "name", "address", "budget")
        self.tree = ttk.Treeview(card_list, columns=cols, show="headings")
        for col in cols: self.tree.heading(col, text=col.capitalize(), anchor="w")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.load_selection)
        
        self.list_companies()

    def create_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Export JSON", command=lambda: self.export_file('json'))
        file_menu.add_command(label="Exit", command=self.quit)

    def create_input(self, parent, label_text, attr_name):
        ttk.Label(parent, text=label_text).pack(anchor="w")
        entry = ttk.Entry(parent)
        entry.pack(fill=tk.X, pady=(0, 8))
        setattr(self, attr_name, entry)

    def save_company(self):
        nit, nom, dire, pre = self.entr_nit.get(), self.entr_name.get(), self.entr_address.get(), self.entr_budget.get()
        try:
            sel = self.tree.selection()
            if sel:
                nit_orig = str(self.tree.item(sel[0])['values'][0])
                self.manager.update_company(nit_orig, nit, nom, dire, pre)
            else:
                self.manager.add_company(nit, nom, dire, pre)
            self.clear_form()
            self.list_companies()
        except Exception as e: messagebox.showerror("Error", str(e))

    def delete_selected(self):
        sel = self.tree.selection()
        if not sel: return
        nit = str(self.tree.item(sel[0])['values'][0])
        self.manager.delete_company(nit)
        self.list_companies()

    def list_companies(self, filter_text=""):
        for i in self.tree.get_children(): self.tree.delete(i)
        for comp in self.manager.companies:
            if filter_text.lower() in comp['name'].lower() or filter_text in str(comp['nit']):
                self.tree.insert("", tk.END, values=(comp['nit'], comp['name'], comp['address'], comp['budget']))

    def filter_list(self, event):
        self.list_companies(self.entr_search.get())

    def load_selection(self, e):
        sel = self.tree.selection()
        if not sel: return
        vals = self.tree.item(sel[0])['values']
        self.clear_form(False)
        self.entr_nit.insert(0, vals[0]); self.entr_name.insert(0, vals[1])
        self.entr_address.insert(0, vals[2]); self.entr_budget.insert(0, vals[3])

    def clear_form(self, clear_selection=True):
        for e in [self.entr_nit, self.entr_name, self.entr_address, self.entr_budget]: e.delete(0, tk.END)

    def export_file(self, file_type):
        path = filedialog.asksaveasfilename(defaultextension=f".{file_type}")
        if path:
            if file_type == 'json': self.manager.export_json(path)
            messagebox.showinfo("Success", "File saved successfully")