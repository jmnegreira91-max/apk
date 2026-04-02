from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard
import yfinance as yf

class SPYBotApp(App):
    def build(self):
        # Diseño Oscuro "Trading Pro"
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
       
        # Etiqueta de Título y Veredicto
        self.label = Label(
            text="[ SERVIDOR DE TRADING CONECTADO ]\nEsperando análisis...",
            font_size='22sp', halign='center', color=(0, 1, 0, 1) # Verde neón
        )
       
        # Botón de Análisis
        self.btn_analizar = Button(
            text="EJECUTAR ANÁLISIS OTM",
            size_hint=(1, 0.3),
            background_color=(0.1, 0.1, 0.1, 1),
            color=(0, 0.8, 1, 1)
        )
        self.btn_analizar.bind(on_press=self.analizar)

        # Botón de Copiar (Aparecerá después de analizar)
        self.btn_copiar = Button(
            text="COPIAR SÍMBOLO PARA BROKER",
            size_hint=(1, 0.2),
            background_color=(0.2, 0.2, 0.2, 1),
            disabled=True
        )
        self.btn_copiar.bind(on_press=self.copiar_codigo)

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.btn_analizar)
        self.layout.add_widget(self.btn_copiar)
       
        self.ultimo_simbolo = ""
        return self.layout

    def analizar(self, instance):
        try:
            spy = yf.Ticker("SPY")
            precio = spy.history(period="1d")['Close'].iloc[-1]
           
            # Lógica OTM (1.5% fuera del dinero)
            strike_call = round(precio * 1.015)
            # Ejemplo de código OCC (AñoMesDia + C/P + Strike)
            self.ultimo_simbolo = f"SPY260415C00{strike_call}000"
           
            self.label.text = f"PRECIO SPY: ${precio:.2f}\nVEREDICTO: COMPRAR CALL\nSTRIKE OTM: ${strike_call}"
            self.btn_copiar.disabled = False
            self.btn_copiar.text = f"COPIAR: {self.ultimo_simbolo}"
        except:
            self.label.text = "⚠️ Error de conexión.\nRevisa tu Internet."

    def copiar_codigo(self, instance):
        Clipboard.copy(self.ultimo_simbolo)
        self.btn_copiar.text = "✅ ¡COPIADO!"

if __name__ == "__main__":
    SPYBotApp().run()