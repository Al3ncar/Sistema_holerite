import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

from employee_service import (
    register_employee,
    list_employees,
    calculate_paycheck,
)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.title("Sistema de Folha de Pagamento")


window.update_idletasks()
width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight() + 100

width_window = int(width_screen * 0.80)
height_window = int(height_screen * 0.70)


pos_x = int((width_screen - width_window) / 2)
pos_y = int((height_screen - height_window) / 2)

window.geometry(f"{width_window}x{height_window}")
window.resizable(False, False)

BG = "#09090b"  
SURFACE = "#18181b"  
SURFACE2 = "#27272a" 
BORDER = "#3f3f46" 
ACCENT = "#2563eb"  
ACCENT_H = "#1d4ed8"  
SUCCESS = "#22c55e"  
TEXT = "#fafafa"  
SUBTEXT = "#a1a1aa"  
MUTED = "#52525b"  
CYAN = "#38bdf8"  

FONT_HERO = ("Georgia", 26, "bold")
FONT_TITLE = ("Georgia", 20, "bold")
FONT_LABEL = ("Helvetica Neue", 13)
FONT_SMALL = ("Helvetica Neue", 12)
FONT_MONO = ("Courier New", 13)
FONT_BUTTON = ("Helvetica Neue", 13, "bold")
FONT_NAV = ("Helvetica Neue", 12)



window.configure(fg_color=BG)


sidebar = ctk.CTkFrame(window, width=220, fg_color=SURFACE, corner_radius=0)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)


content_area = ctk.CTkFrame(window, fg_color=BG, corner_radius=0)
content_area.pack(side="right", fill="both", expand=True)

logo_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
logo_frame.pack(fill="x", padx=24, pady=(32, 8))

logo_dot = ctk.CTkLabel(
    logo_frame,
    text="●",
    font=("Georgia", 18),
    text_color=ACCENT,
)
logo_dot.pack(side="left", padx=(0, 8))

logo_label = ctk.CTkLabel(
    logo_frame,
    text="Payroll",
    font=("Georgia", 16, "bold"),
    text_color=TEXT,
)
logo_label.pack(side="left")

ctk.CTkFrame(sidebar, height=1, fg_color=BORDER).pack(fill="x", padx=24, pady=(16, 24))

ctk.CTkLabel(
    sidebar,
    text="NAVEGAÇÃO",
    font=("Helvetica Neue", 11, "bold"),
    text_color=MUTED,
).pack(anchor="w", padx=24, pady=(0, 12))

_active_nav = {"btn": None, "icon": None, "text": None}


def make_nav_button(parent, icon, label):
    frame = ctk.CTkFrame(parent, fg_color="transparent", cursor="hand2")
    frame.pack(fill="x", padx=12, pady=2)

    inner = ctk.CTkFrame(frame, fg_color="transparent", corner_radius=8, cursor="hand2")
    inner.pack(fill="x")

    icon_lbl = ctk.CTkLabel(
        inner, text=icon, font=("Helvetica Neue", 14), text_color=SUBTEXT, width=28
    )
    icon_lbl.pack(side="left", padx=(8, 6), pady=5)

    text_lbl = ctk.CTkLabel(
        inner, text=label, font=FONT_NAV, text_color=SUBTEXT, anchor="w"
    )
    text_lbl.pack(side="left", pady=5)

    def set_active():
        prev = _active_nav["btn"]
        if prev and prev != inner:
            prev.configure(fg_color="transparent")
            if _active_nav["icon"]:
                _active_nav["icon"].configure(text_color=SUBTEXT)
            if _active_nav["text"]:
                _active_nav["text"].configure(text_color=SUBTEXT)
        inner.configure(fg_color=SURFACE2)
        icon_lbl.configure(text_color=TEXT)
        text_lbl.configure(text_color=TEXT)
        _active_nav["btn"] = inner
        _active_nav["icon"] = icon_lbl
        _active_nav["text"] = text_lbl

    def on_enter(e):
        if inner != _active_nav["btn"]:
            inner.configure(fg_color="#332d2d")

    def on_leave(e):
        if inner != _active_nav["btn"]:
            inner.configure(fg_color="transparent")

    for w in [frame, inner, icon_lbl, text_lbl]:
        w.bind("<Enter>", on_enter)
        w.bind("<Leave>", on_leave)

    return inner, set_active, icon_lbl, text_lbl


nav_home_inner, nav_home_activate, nav_home_icon, nav_home_text = make_nav_button(
    sidebar, "⌂", "Início"
)
nav_reg_inner, nav_reg_activate, nav_reg_icon, nav_reg_text = make_nav_button(
    sidebar, "+", "1. Cadastrar Funcionário"
)
nav_emp_inner, nav_emp_activate, nav_emp_icon, nav_emp_text = make_nav_button(
    sidebar, "≡", "2. Ver Funcionários"
)

ctk.CTkFrame(sidebar, height=1, fg_color=BORDER).pack(
    fill="x", padx=24, pady=(0, 16), side="bottom"
)
ctk.CTkLabel(
    sidebar,
    text="v1.0.0  ·  Sistema RH",
    font=("Helvetica Neue", 12),
    text_color=MUTED,
).pack(side="bottom", pady=(0, 4))

home_screen = ctk.CTkFrame(content_area, fg_color="transparent")
register_screen = ctk.CTkFrame(content_area, fg_color="transparent")
employee_screen = ctk.CTkFrame(content_area, fg_color="transparent")


def clear_screen():
    home_screen.pack_forget()
    register_screen.pack_forget()
    employee_screen.pack_forget()


def go_home():
    clear_screen()
    nav_home_activate()  
    home_screen.pack(fill="both", expand=True)


def open_register_screen():
    clear_screen()
    nav_reg_activate()  
    register_screen.pack(fill="both", expand=True)


def open_employee_screen():
    clear_screen()
    nav_emp_activate() 
    employee_screen.pack(fill="both", expand=True)
    update_employee_list()



for _w in [nav_home_inner, nav_home_icon, nav_home_text]:
    _w.bind("<Button-1>", lambda e: go_home())
for _w in [nav_reg_inner, nav_reg_icon, nav_reg_text]:
    _w.bind("<Button-1>", lambda e: open_register_screen())
for _w in [nav_emp_inner, nav_emp_icon, nav_emp_text]:
    _w.bind("<Button-1>", lambda e: open_employee_screen())


home_center = ctk.CTkFrame(home_screen, fg_color="transparent")
home_center.pack(expand=True) 

ctk.CTkLabel(
    home_center,
    text="Folha de Pagamento",
    font=FONT_HERO,
    text_color=TEXT,
).pack(pady=(0, 6))

ctk.CTkLabel(
    home_center,
    text="Gerencie seus colaboradores e holerites em um só lugar.",
    font=FONT_LABEL,
    text_color=SUBTEXT,
).pack(pady=(0, 48))

cards_row = ctk.CTkFrame(home_center, fg_color="transparent")
cards_row.pack()


def create_home_card(parent, icon, title, desc, command):
    card = ctk.CTkFrame(
        parent,
        width=270,
        height=215,
        fg_color=SURFACE,
        corner_radius=16,
        border_width=1,
        border_color=BORDER,
        cursor="hand2",
    )
    card.pack(side="left", padx=14)
    card.pack_propagate(False)

 
    ctk.CTkFrame(card, fg_color="transparent", height=28).pack()

    icon_frame = ctk.CTkFrame(
        card, width=48, height=48, fg_color="#1e3a5f", corner_radius=12
    )
    icon_frame.pack()
    icon_frame.pack_propagate(False)
    ctk.CTkLabel(
        icon_frame, text=icon, font=("Helvetica Neue", 22), text_color=ACCENT
    ).place(relx=0.5, rely=0.5, anchor="center")

    title_lbl = ctk.CTkLabel(
        card, text=title, font=("Georgia", 13, "bold"), text_color=TEXT
    )
    title_lbl.pack(pady=(14, 4))

    desc_lbl = ctk.CTkLabel(
        card, text=desc, font=FONT_SMALL, text_color=SUBTEXT, justify="center"
    )
    desc_lbl.pack()

    def on_enter(e):
        card.configure(fg_color=SURFACE2, border_color=ACCENT)

    def on_leave(e):
        card.configure(fg_color=SURFACE, border_color=BORDER)

    for w in [card, icon_frame, title_lbl, desc_lbl]:
        w.bind("<Button-1>", lambda e: command())
        w.bind("<Enter>", on_enter)
        w.bind("<Leave>", on_leave)

    return card


create_home_card(
    cards_row,
    "+",
    "1. Cadastrar Funcionário",
    "Adicione novos colaboradores\nao sistema.",
    open_register_screen,
)

create_home_card(
    cards_row,
    "≡",
    "2. Ver Funcionários",
    "Liste colaboradores\ne gere holerites.",
    open_employee_screen,
)

reg_outer = ctk.CTkFrame(register_screen, fg_color="transparent")
reg_outer.pack(fill="both", expand=True, padx=60, pady=32)

reg_header = ctk.CTkFrame(reg_outer, fg_color="transparent")
reg_header.pack(fill="x", pady=(0, 24))

ctk.CTkLabel(
    reg_header,
    text="Cadastrar Funcionário",
    font=FONT_TITLE,
    text_color=TEXT,
).pack(anchor="w")

ctk.CTkLabel(
    reg_header,
    text="Preencha os dados abaixo para registrar um novo colaborador.",
    font=FONT_SMALL,
    text_color=SUBTEXT,
).pack(anchor="w", pady=(4, 0))

form_card = ctk.CTkFrame(
    reg_outer,
    fg_color=SURFACE,
    corner_radius=16,
    border_width=1,
    border_color=BORDER,
)
form_card.pack(fill="x")

form_inner = ctk.CTkFrame(form_card, fg_color="transparent")
form_inner.pack(padx=40, pady=36, fill="x")


def create_field(parent, label_text, placeholder=""):
    ctk.CTkLabel(
        parent,
        text=label_text,
        font=("Helvetica Neue", 11, "bold"),
        text_color=SUBTEXT,
    ).pack(anchor="w", pady=(0, 6))

    entry = ctk.CTkEntry(
        parent,
        placeholder_text=placeholder,
        font=FONT_LABEL,
        fg_color=SURFACE2,
        border_color=BORDER,
        border_width=1,
        corner_radius=8,
        height=42,
        text_color=TEXT,
        placeholder_text_color=MUTED,
    )
    entry.pack(fill="x", pady=(0, 18))
    return entry


entry_name = create_field(form_inner, "Nome completo", "Ex: João da Silva")
entry_role = create_field(form_inner, "Cargo", "Ex: Analista de Sistemas")
entry_dependents = create_field(form_inner, "Dependentes", "Ex: 2")
entry_salary = create_field(form_inner, "Salário Bruto (R$)", "Ex: 5000.00")

btn_row = ctk.CTkFrame(form_inner, fg_color="transparent")
btn_row.pack(fill="x", pady=(4, 0))


def clear_fields():
    entry_name.delete(0, tk.END)
    entry_role.delete(0, tk.END)
    entry_dependents.delete(0, tk.END)
    entry_salary.delete(0, tk.END)


def register():
    name = entry_name.get().strip()
    role = entry_role.get().strip()

    if not name or not role:
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return

    try:
        dependents = int(entry_dependents.get())
        gross_salary = float(entry_salary.get())
    except ValueError:
        messagebox.showerror("Erro", "Valores inválidos.")
        return

    success = register_employee(name, role, dependents, gross_salary)

    if not success:
        messagebox.showerror("Erro", "Funcionário já cadastrado.")
        return

    messagebox.showinfo("Sucesso", "Funcionário cadastrado com sucesso.")
    clear_fields()


ctk.CTkButton(
    btn_row,
    text="Limpar campos",
    font=FONT_BUTTON,
    fg_color="transparent",
    border_color=BORDER,
    border_width=1,
    hover_color=SURFACE2,
    text_color=SUBTEXT,
    corner_radius=8,
    height=42,
    command=clear_fields,
).pack(side="left", expand=True, fill="x", padx=(0, 8))

ctk.CTkButton(
    btn_row,
    text="Cadastrar  →",
    font=FONT_BUTTON,
    fg_color=ACCENT,
    hover_color=ACCENT_H,
    text_color="white",
    corner_radius=8,
    height=42,
    command=register,
).pack(side="left", expand=True, fill="x")

emp_outer = ctk.CTkFrame(employee_screen, fg_color="transparent")
emp_outer.pack(fill="both", expand=True, padx=36, pady=32)

emp_header = ctk.CTkFrame(emp_outer, fg_color="transparent")
emp_header.pack(fill="x", pady=(0, 20))

ctk.CTkLabel(
    emp_header,
    text="Funcionários",
    font=FONT_TITLE,
    text_color=TEXT,
).pack(side="left")

ctk.CTkLabel(
    emp_header,
    text="Selecione um colaborador para visualizar o holerite",
    font=FONT_SMALL,
    text_color=SUBTEXT,
).pack(side="left", padx=(14, 0), pady=(4, 0))

panels = ctk.CTkFrame(emp_outer, fg_color="transparent")
panels.pack(fill="both", expand=True)

left_panel = ctk.CTkFrame(
    panels,
    fg_color=SURFACE,
    corner_radius=16,
    border_width=1,
    border_color=BORDER,
    width=340,
)
left_panel.pack(side="left", fill="y", padx=(0, 14))
left_panel.pack_propagate(False)

ctk.CTkLabel(
    left_panel,
    text="Lista de Colaboradores",
    font=("Helvetica Neue", 11, "bold"),
    text_color=SUBTEXT,
).pack(anchor="w", padx=20, pady=(18, 10))

ctk.CTkFrame(left_panel, height=1, fg_color=BORDER).pack(fill="x", padx=0)

import tkinter.ttk as ttk

style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Payroll.Treeview",
    background=SURFACE,
    foreground=TEXT,
    fieldbackground=SURFACE,
    rowheight=46,
    borderwidth=0,
    font=("Helvetica Neue", 11),
)
style.configure(
    "Payroll.Treeview.Heading",
    background=SURFACE2,
    foreground=SUBTEXT,
    relief="flat",
    font=("Helvetica Neue", 10, "bold"),
    borderwidth=0,
)
style.map(
    "Payroll.Treeview",
    background=[("selected", "#1e3a5f")],
    foreground=[("selected", TEXT)],
)
style.layout("Payroll.Treeview", [("Treeview.treearea", {"sticky": "nswe"})])

tree_frame = tk.Frame(left_panel, bg=SURFACE)
tree_frame.pack(fill="both", expand=True, padx=0, pady=0)

tree = ttk.Treeview(
    tree_frame,
    columns=("nome", "cargo"),
    show="headings",
    selectmode="browse",
    style="Payroll.Treeview",
)

tree.heading("nome", text="Nome", anchor="w")
tree.heading("cargo", text="Cargo", anchor="w")
tree.column("nome", anchor="w", width=160, minwidth=100)
tree.column("cargo", anchor="w", width=160, minwidth=100)

scrollbar = ctk.CTkScrollbar(
    tree_frame, command=tree.yview, button_color=BORDER, fg_color=SURFACE
)
tree.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
tree.pack(side="left", fill="both", expand=True)


right_panel = ctk.CTkFrame(
    panels,
    fg_color=SURFACE,
    corner_radius=16,
    border_width=1,
    border_color=BORDER,
)
right_panel.pack(side="right", fill="both", expand=True)

pay_header = ctk.CTkFrame(right_panel, fg_color="transparent")
pay_header.pack(fill="x", padx=24, pady=(18, 0))

ctk.CTkLabel(
    pay_header,
    text="Holerite",
    font=("Helvetica Neue", 13, "bold"),
    text_color=SUBTEXT,
).pack(side="left")

badge = ctk.CTkLabel(
    pay_header,
    text="  Mensal  ",
    font=("Helvetica Neue", 12, "bold"),
    text_color=SUCCESS,
    fg_color="#14532d",
    corner_radius=4,
)
badge.pack(side="left", padx=10)

ctk.CTkFrame(right_panel, height=1, fg_color=BORDER).pack(
    fill="x", padx=0, pady=(14, 0)
)

placeholder_frame = ctk.CTkFrame(right_panel, fg_color="transparent")
placeholder_frame.pack(expand=True)

placeholder_icon = ctk.CTkLabel(
    placeholder_frame,
    text="◎",
    font=("Georgia", 36),
    text_color=BORDER,
)
placeholder_icon.pack(pady=(0, 12))

placeholder_text = ctk.CTkLabel(
    placeholder_frame,
    text="Selecione um colaborador\nna lista ao lado",
    font=FONT_LABEL,
    text_color=MUTED,
    justify="center",
)
placeholder_text.pack()

pay_content = ctk.CTkScrollableFrame(
    right_panel,
    fg_color="transparent",
    scrollbar_button_color=BORDER,
)


def _row(parent, label, value, label_color=SUBTEXT, value_color=TEXT, value_font=None):
    """Helper: render a label/value pair as a horizontal row."""
    row = ctk.CTkFrame(parent, fg_color="transparent")
    row.pack(fill="x", pady=3)
    ctk.CTkLabel(
        row, text=label, font=FONT_LABEL, text_color=label_color, anchor="w"
    ).pack(side="left")
    ctk.CTkLabel(
        row,
        text=value,
        font=value_font or FONT_LABEL,
        text_color=value_color,
        anchor="e",
    ).pack(side="right")


def _divider(parent):
    ctk.CTkFrame(parent, height=1, fg_color=BORDER).pack(fill="x", pady=12)


def show_paycheck(event):
    selected = tree.selection()
    if not selected:
        return

    item = tree.item(selected[0])
    emp_name = item["values"][0]
    paycheck = calculate_paycheck(emp_name)

    for w in pay_content.winfo_children():
        w.destroy()

    placeholder_frame.pack_forget()
    pay_content.pack(fill="both", expand=True, padx=28, pady=20)

    info = ctk.CTkFrame(pay_content, fg_color=SURFACE2, corner_radius=12)
    info.pack(fill="x", pady=(0, 20))

    info_inner = ctk.CTkFrame(info, fg_color="transparent")
    info_inner.pack(padx=20, pady=14, fill="x")

    avatar = ctk.CTkFrame(
        info_inner, width=46, height=46, fg_color="#1e3a5f", corner_radius=23
    )
    avatar.pack(side="left", padx=(0, 14))
    avatar.pack_propagate(False)
    ctk.CTkLabel(
        avatar,
        text=paycheck["name"][0].upper(),
        font=("Georgia", 18, "bold"),
        text_color=ACCENT,
    ).place(relx=0.5, rely=0.5, anchor="center")

    info_text = ctk.CTkFrame(info_inner, fg_color="transparent")
    info_text.pack(side="left")
    ctk.CTkLabel(
        info_text,
        text=paycheck["name"],
        font=("Georgia", 13, "bold"),
        text_color=TEXT,
        anchor="w",
    ).pack(anchor="w")
    ctk.CTkLabel(
        info_text,
        text=paycheck["role"],
        font=FONT_SMALL,
        text_color=SUBTEXT,
        anchor="w",
    ).pack(anchor="w")

    ctk.CTkLabel(
        pay_content,
        text="REMUNERAÇÃO BRUTA",
        font=("Helvetica Neue", 12, "bold"),
        text_color=MUTED,
    ).pack(anchor="w", pady=(0, 6))

    sal_card = ctk.CTkFrame(pay_content, fg_color=SURFACE2, corner_radius=10)
    sal_card.pack(fill="x")
    sal_inner = ctk.CTkFrame(sal_card, fg_color="transparent")
    sal_inner.pack(padx=18, pady=14, fill="x")
    _row(
        sal_inner,
        "Salário Bruto",
        f"R$ {paycheck['gross_salary']:,.2f}",
        value_font=("Helvetica Neue", 13, "bold"),
        value_color=TEXT,
    )

    _divider(pay_content)

    ctk.CTkLabel(
        pay_content,
        text="DESCONTOS",
        font=("Helvetica Neue", 10, "bold"),
        text_color=MUTED,
    ).pack(anchor="w", pady=(0, 6))

    ded_card = ctk.CTkFrame(pay_content, fg_color=SURFACE2, corner_radius=10)
    ded_card.pack(fill="x")
    ded_inner = ctk.CTkFrame(ded_card, fg_color="transparent")
    ded_inner.pack(padx=18, pady=14, fill="x")
    _row(ded_inner, "(-) INSS", f"R$ {paycheck['inss']:,.2f}", value_color="#f87171")
    _row(ded_inner, "(-) IRRF", f"R$ {paycheck['irrf']:,.2f}", value_color="#f87171")

    _divider(pay_content)

    net_card = ctk.CTkFrame(
        pay_content,
        fg_color="#1a2e1a",
        corner_radius=10,
        border_width=1,
        border_color="#166534",
    )
    net_card.pack(fill="x")
    net_inner = ctk.CTkFrame(net_card, fg_color="transparent")
    net_inner.pack(padx=18, pady=16, fill="x")
    _row(
        net_inner,
        "Salário Líquido",
        f"R$ {paycheck['net_salary']:,.2f}",
        label_color=SUCCESS,
        value_color=SUCCESS,
        value_font=("Georgia", 15, "bold"),
    )

    _divider(pay_content)

    ctk.CTkLabel(
        pay_content,
        text="ENCARGOS (empresa)",
        font=("Helvetica Neue", 12, "bold"),
        text_color=MUTED,
    ).pack(anchor="w", pady=(0, 6))

    fgts_card = ctk.CTkFrame(pay_content, fg_color=SURFACE2, corner_radius=10)
    fgts_card.pack(fill="x", pady=(0, 20))
    fgts_inner = ctk.CTkFrame(fgts_card, fg_color="transparent")
    fgts_inner.pack(padx=18, pady=14, fill="x")
    _row(fgts_inner, "FGTS (8%)", f"R$ {paycheck['fgts']:,.2f}", value_color=CYAN)


tree.bind("<<TreeviewSelect>>", show_paycheck)


def update_employee_list():
    for row in tree.get_children():
        tree.delete(row)

    for emp_name in list_employees():
        paycheck = calculate_paycheck(emp_name)
        tree.insert("", "end", values=(paycheck["name"], paycheck["role"]))

    for w in pay_content.winfo_children():
        w.destroy()
    pay_content.pack_forget()
    placeholder_frame.pack(expand=True)


go_home()


def start_system():
    window.mainloop()
