import PySimpleGUI as sg

sg.ChangeLookAndFeel("DarkBrown") # Temas

WIN_W = 90
WIN_H = 25
filename = None

file_new = "Novo        (CTRL+G)"
file_open = "Abrir      (CTR+O)"
file_save = "Salva Arquivo      (CTRL+S)"

sg.Text()
menu_layout = (
    ["Arquivo", [file_new, file_open, file_save, "Salvar Como", "---", "Sair"]],
    ["Editar", ["Caixa Alta", "Caixa Baixa"]],
    ["Ajuda", ["OI"]],
)

layout = [
    [sg.MenuBar(menu_layout)],
    [
        sg.Multiline(
            font=("Consolas", 15), text_color="white", size=(WIN_W, WIN_H), key="_BODY_"
        )
    ],
]

window = sg.Window(
    "Bloco de Notas",
    layout=layout,
    margins=(0, 0),
    resizable=True,
    return_keyboard_events=True,
)
window.read(timeout=1)

window["_BODY_"].expand(expand_x=True, expand_y=True)


def new_file() -> str:
    window["_BODY_"].update(value="")
    filename = None
    return filename


def open_file() -> str:
    try:
        filename: str = sg.popup_get_file("Open File", no_window=True)
    except:
        return
    if filename not in (None, "") and not isinstance(filename, tuple):
        with open(filename, "r") as f:
            window["_BODY_"].update(value=f.read())
        return filename


def save_file(filename: str):
    if filename not in (None, ""):
        with open(filename, "w") as f:
            f.write(values.get("_BODY_"))
    else:
        save_file_as()


def save_file_as() -> str:
    try:
        filename: str = sg.popup_get_file(
            "Save File",
            save_as=True,
            no_window=True,
            default_extension=".txt",
            file_types=(("Text", ".txt"),),
        )
    except:
        return
    if filename not in (None, "") and not isinstance(filename, tuple):
        with open(filename, "w") as f:
            f.write(values.get("_BODY_"))
    return filename


def caixa_baixa():
    window["_BODY_"].update(value=str(values["_BODY_"]).lower())


def caixa_alta():
    window["_BODY_"].update(value=str(values["_BODY_"]).upper())


while True:
    event, values = window.read()

    if event  in (None, "Exit"):
        window.close()
        break
    if event in (file_new, "n:77"):
        filename = new_file()
    if event in (file_open, "o:78"):
        filename = open_file()
    if event in (file_save, "s:83"):
        save_file(filename)
    if event in ("Save As",):
        filename = save_file_as()
    if event == "Caixa Alta":
        caixa_alta()
    if event == "Caixa Baixa":
        caixa_baixa()

Notepad = Notepad()
Notepad.Iniciar()