import tkinter as tk
from tkinter import messagebox

from employee_service import (
    register_employee,
    list_employees,
    calculate_paycheck,
)

# =====================================
# CONFIG
# =====================================

window = tk.Tk()
window.title('Sistema de Folha de Pagamento')
window.geometry('1100x700')
window.configure(bg='#020617')

# =====================================
# COLORS
# =====================================

BG = '#020617'
CARD = '#0f172a'
CARD_HOVER = '#111c34'
BLUE = '#2563eb'
TEXT = '#f8fafc'
SUBTEXT = '#94a3b8'
INPUT = '#1e293b'
BORDER = '#334155'

FONT_TITLE = ('Segoe UI', 28, 'bold')
FONT_SUBTITLE = ('Segoe UI', 12)
FONT_CARD_TITLE = ('Segoe UI', 18, 'bold')
FONT_TEXT = ('Segoe UI', 11)
FONT_BUTTON = ('Segoe UI', 11, 'bold')

# =====================================
# MAIN CONTAINER
# =====================================

main_container = tk.Frame(window, bg=BG)
main_container.pack(fill='both', expand=True)

# =====================================
# HOME SCREEN
# =====================================

home_screen = tk.Frame(main_container, bg=BG)
home_screen.pack(fill='both', expand=True)

title = tk.Label(
    home_screen,
    text='Sistema de Folha de Pagamento',
    bg=BG,
    fg=TEXT,
    font=FONT_TITLE,
)

title.pack(pady=(60, 10))

subtitle = tk.Label(
    home_screen,
    text='Escolha uma opção abaixo',
    bg=BG,
    fg=SUBTEXT,
    font=FONT_SUBTITLE,
)

subtitle.pack(pady=(0, 40))

cards_container = tk.Frame(home_screen, bg=BG)
cards_container.pack()


# =====================================
# REGISTER SCREEN
# =====================================

register_screen = tk.Frame(main_container, bg=BG)

# =====================================
# EMPLOYEE SCREEN
# =====================================

employee_screen = tk.Frame(main_container, bg=BG)

# =====================================
# FUNCTIONS
# =====================================


def clear_screen():
    home_screen.pack_forget()
    register_screen.pack_forget()
    employee_screen.pack_forget()


def go_home():
    clear_screen()
    home_screen.pack(fill='both', expand=True)


def open_register_screen():
    clear_screen()
    register_screen.pack(fill='both', expand=True)


def open_employee_screen():
    clear_screen()
    employee_screen.pack(fill='both', expand=True)
    update_employee_list()


def create_card(parent, title, description, command):
    card = tk.Frame(
        parent,
        bg=CARD,
        width=320,
        height=220,
        cursor='hand2',
        highlightbackground=BORDER,
        highlightthickness=1,
    )

    card.pack(side='left', padx=20)

    card.pack_propagate(False)

    def on_enter(event):
        card.config(bg=CARD_HOVER)

    def on_leave(event):
        card.config(bg=CARD)

    card.bind('<Enter>', on_enter)
    card.bind('<Leave>', on_leave)
    card.bind('<Button-1>', lambda event: command())

    title_label = tk.Label(
        card,
        text=title,
        bg=CARD,
        fg=TEXT,
        font=FONT_CARD_TITLE,
    )

    title_label.pack(pady=(50, 10))

    desc_label = tk.Label(
        card,
        text=description,
        bg=CARD,
        fg=SUBTEXT,
        font=FONT_TEXT,
        justify='center',
    )

    desc_label.pack(padx=20)

    title_label.bind(
        '<Button-1>',
        lambda event: command(),
    )

    desc_label.bind(
        '<Button-1>',
        lambda event: command(),
    )

    return card


# =====================================
# HOME CARDS
# =====================================

create_card(
    cards_container,
    '1. Cadastrar Funcionário',
    'Cadastre novos funcionários\nno sistema.',
    open_register_screen,
)

create_card(
    cards_container,
    '2. Ver Funcionários',
    'Visualize funcionários\n e gere holerites.',
    open_employee_screen,
)

# =====================================
# REGISTER PAGE
# =====================================

register_title = tk.Label(
    register_screen,
    text='Cadastrar Funcionário',
    bg=BG,
    fg=TEXT,
    font=FONT_TITLE,
)

register_title.pack(pady=(40, 20))

form_card = tk.Frame(
    register_screen,
    bg=CARD,
    width=500,
    height=450,
    highlightbackground=BORDER,
    highlightthickness=1,
)

form_card.pack()

form_card.pack_propagate(False)

form = tk.Frame(form_card, bg=CARD)
form.pack(pady=30)


def create_label(parent, text):
    return tk.Label(
        parent,
        text=text,
        bg=CARD,
        fg=SUBTEXT,
        font=FONT_TEXT,
        anchor='w',
    )


def create_input(parent):
    return tk.Entry(
        parent,
        bg=INPUT,
        fg=TEXT,
        relief='flat',
        font=FONT_TEXT,
        insertbackground=TEXT,
        width=35,
    )


# Nome

create_label(form, 'Nome').pack(anchor='w', pady=(10, 5))
entry_name = create_input(form)
entry_name.pack(ipady=8)

# Cargo

create_label(form, 'Cargo').pack(anchor='w', pady=(15, 5))
entry_role = create_input(form)
entry_role.pack(ipady=8)

# Dependentes

create_label(form, 'Dependentes').pack(anchor='w', pady=(15, 5))
entry_dependents = create_input(form)
entry_dependents.pack(ipady=8)

# Salário

create_label(form, 'Salário Bruto').pack(anchor='w', pady=(15, 5))
entry_salary = create_input(form)
entry_salary.pack(ipady=8)


def clear_fields():
    entry_name.delete(0, tk.END)
    entry_role.delete(0, tk.END)
    entry_dependents.delete(0, tk.END)
    entry_salary.delete(0, tk.END)


def register():
    name = entry_name.get().strip()
    role = entry_role.get().strip()

    if not name or not role:
        messagebox.showerror(
            'Erro',
            'Preencha todos os campos.'
        )
        return

    try:
        dependents = int(entry_dependents.get())
        gross_salary = float(entry_salary.get())
    except ValueError:
        messagebox.showerror(
            'Erro',
            'Valores inválidos.'
        )
        return

    success = register_employee(
        name,
        role,
        dependents,
        gross_salary,
    )

    if not success:
        messagebox.showerror(
            'Erro',
            'Funcionário já cadastrado.'
        )
        return

    messagebox.showinfo(
        'Sucesso',
        'Funcionário cadastrado.'
    )

    clear_fields()


button_register = tk.Button(
    form_card,
    text='Cadastrar',
    bg=BLUE,
    fg='white',
    relief='flat',
    cursor='hand2',
    font=FONT_BUTTON,
    activebackground='#1d4ed8',
    activeforeground='white',
    command=register,
)

button_register.pack(ipadx=20, ipady=10)

button_back = tk.Button(
    register_screen,
    text='← Voltar',
    bg=BG,
    fg=SUBTEXT,
    relief='flat',
    cursor='hand2',
    font=FONT_TEXT,
    command=go_home,
)

button_back.pack(pady=20)

# =====================================
# EMPLOYEE SCREEN
# =====================================

employee_title = tk.Label(
    employee_screen,
    text='Funcionários',
    bg=BG,
    fg=TEXT,
    font=FONT_TITLE,
)

employee_title.pack(pady=(40, 20))

employee_card = tk.Frame(
    employee_screen,
    bg=CARD,
    width=850,
    height=500,
    highlightbackground=BORDER,
    highlightthickness=1,
)

employee_card.pack()

employee_card.pack_propagate(False)

content = tk.Frame(employee_card, bg=CARD)
content.pack(fill='both', expand=True, padx=20, pady=20)

# LISTA

listbox = tk.Listbox(
    content,
    bg=INPUT,
    fg=TEXT,
    relief='flat',
    font=('Consolas', 11),
    width=25,
    highlightthickness=0,
    selectbackground=BLUE,
)

listbox.pack(side='left', fill='y')

# HOLLERITH

text_result = tk.Text(
    content,
    bg='#020617',
    fg='#38bdf8',
    relief='flat',
    font=('Consolas', 11),
    insertbackground='white',
)

text_result.pack(
    side='right',
    fill='both',
    expand=True,
    padx=(20, 0),
)


def update_employee_list():
    listbox.delete(0, tk.END)

    for employee in list_employees():
        listbox.insert(tk.END, employee)


def show_paycheck(event):
    selection = listbox.curselection()

    if not selection:
        return

    employee_name = listbox.get(selection[0])

    paycheck = calculate_paycheck(employee_name)

    text_result.delete('1.0', tk.END)

    result = f'''
═══════════════════════════════════════
             HOLLERITH
═══════════════════════════════════════

Funcionário:
{paycheck["name"]}

Cargo:
{paycheck["role"]}

───────────────────────────────────────

Salário Bruto:
R$ {paycheck["gross_salary"]:.2f}

(-) INSS:
R$ {paycheck["inss"]:.2f}

(-) IRRF:
R$ {paycheck["irrf"]:.2f}

───────────────────────────────────────

Salário Líquido:
R$ {paycheck["net_salary"]:.2f}

───────────────────────────────────────

FGTS:
R$ {paycheck["fgts"]:.2f}

═══════════════════════════════════════
'''

    text_result.insert(tk.END, result)


listbox.bind('<<ListboxSelect>>', show_paycheck)

button_back_employee = tk.Button(
    employee_screen,
    text='← Voltar',
    bg=BG,
    fg=SUBTEXT,
    relief='flat',
    cursor='hand2',
    font=FONT_TEXT,
    command=go_home,
)

button_back_employee.pack(pady=20)

def start_system():
    window.mainloop()