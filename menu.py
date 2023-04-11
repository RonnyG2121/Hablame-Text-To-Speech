# Creando el módulo del menú
import wx

class Barra_Menu(wx.MenuBar):
    def __init__(self):
        super(Barra_Menu, self).__init__()
        self.MenuPrincipal()
    # Creando el menú
    def MenuPrincipal(self):
        # Objeto de tipo menú
        archivo = wx.Menu()
        # Creando los items de Menú
        salir = wx.MenuItem(archivo, wx.ID_EXIT, "&salir\Ctrl+s", "Cierra la aplicación")
        guardar = wx.MenuItem(archivo, wx.ID_SAVE, "&Guardar en mp3\tCtrl+g", "Guarda el texto en un archivo de audio")
        # Añadiendo los items al menú
        archivo.Append(salir)
        archivo.Append(guardar)
        self.Append(archivo, "&Menú de opciones")
        

