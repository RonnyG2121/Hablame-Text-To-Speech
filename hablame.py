# Creando Conversor de texto a voz con wxpython
import wx
from menu import Barra_Menu
import accessible_output3

# Creando clase conversor
class Conversor(wx.Frame):
    def __init__(self, parent):
        super(Conversor, self).__init__(parent)
        # instanciando la clase Barra_Menu que contiene un menú de opciones
        self.barra_Menu = Barra_Menu()
        # Estableciendo la barra de menú
        self.SetMenuBar(self.barra_Menu)
        # Estableciendo mis propiedades o características que tengrá este conversor de texto a voz
        self.SetSize((800, 600))
        self.Centre()
        self.SetTitle("Háblame")
        self.Show(True)

        # Llamando método que creará la interface gráfica
        self.InitUI()

    # método que crea la interface
    def InitUI(self):
        # Creando un panel
        panel = wx.Panel(self, wx.ID_ANY)
        # Creando contenedor para los elementos de la interface
        grid = wx.GridSizer(11, 1, 0, 0)

        # Creando el combobox para elegir las voces instaladas
        label_combo_box = wx.StaticText(panel, wx.ID_ANY, "Seleccione una voz")
        combo_box = wx.ComboBox(panel, wx.ID_ANY, choices=[], style=wx.TE_READONLY)

        # Creando el textbox multilínea y su label correspondiente para escribir el texto
        label_Text_CTRL = wx.StaticText(panel, wx.ID_ANY, "Escriba el texto aquí")
        text_ctrl = wx.TextCtrl(panel, wx.ID_ANY, style=wx.TE_MULTILINE | wx.TE_CENTER)
        
        # Creando los botones deslizantes
        label_Slider1 = wx.StaticText(panel, wx.ID_ANY, "Tono")
        slider_1 = wx.Slider(panel, wx.ID_ANY , value=50, minValue=0, maxValue=100)
        label_Slider2 = wx.StaticText(panel, wx.ID_ANY, "Velocidad")
        slider_2 = wx.Slider(panel, value=50, minValue=0, maxValue=100)
        label_Slider3 = wx.StaticText(panel, wx.ID_ANY, "Volumen")
        slider_3 = wx.Slider(panel, value=50, minValue=0, maxValue=100)
        # Creando el botón de lectura 
        leer_button = wx.Button(panel, label="Leer")

        # Agregando los elementos al grid
        grid.AddMany([
            (label_combo_box, 0, wx.ALL, 5),
            (combo_box, 0, wx.ALL, 5),
            (label_Text_CTRL, 0, wx.ALL, 5),
            (text_ctrl, 0, wx.ALL, 5),
            (label_Slider1, 0, wx.ALL, 5),
            (slider_1, 0, wx.ALL, 5),
            (label_Slider2, 0, wx.ALL, 5),
            (slider_2, 0, wx.ALL, 5),
            (label_Slider3, 0, wx.ALL, 5),
            (slider_3, 0, wx.ALL, 5),
            (leer_button, 0, wx.ALL, 5)])
        
        # Estableciendo el panel
        panel.SetSizer(grid)
        panel.Layout()
        panel.SetFocus()
        panel.Fit()




if __name__ == "__main__":
    aplicacion = wx.App()
    Conversor(None)
    aplicacion.MainLoop()