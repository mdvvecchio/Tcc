import kivy
#kivy.require('1.8.0')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider


#class Tela(BoxLayout):
#    pass

red = (255, 0, 0, 1)
green = (0, 255, 0, 1)
yellow = (255,121,0,1)
orange = (120,40,0,1)
fonte = 15

class Main(App):
    """def __init__(self, porta = "", intensidade_m = 0 , intensidade_f = 0, intensidade_t = 0, sentido = 0):
        self.info = {}
        
        self.porta = porta
        self.intensidade_m = intensidade_m
        self.intensidade_f = intensidade_f
        self.intensidade_t = intensidade_t
        self.sentido = sentido
    """    
    
    def OnSliderValueChange_m(self, instance, value):
        self.intensidade_m = value
        self.aciona()
    
    def OnSliderValueChange_f(self, instance, value):
        self.intensidade_f = value
        self.aciona()
        
    def OnSliderValueChange_t(self, instance, value):
        self.intensidade_t = value
        self.aciona()
        
    def build(self):
        
        self.porta = ""
        self.intensidade_m = 0
        self.intensidade_f = 0
        self.intensidade_t = 0
        self.sentido = False
        
        tela = BoxLayout(orientation = 'vertical')
        frame0 = BoxLayout(orientation = 'horizontal')
        
        intens_lf = Slider(min=0, max = 255, value = 0, step = 1, orientation = 'vertical')
        self.btn_luz_frente = Button(text = 'OFF', background_color = red)
        lb_luz_frente = Label(text = 'Controle da Luz Dianteira', font_size = fonte)
        frame0.add_widget(lb_luz_frente)
        frame0.add_widget(self.btn_luz_frente)
        frame0.add_widget(intens_lf)
        intens_lf.bind(value=self.OnSliderValueChange_f)
        
        frame1 = BoxLayout(orientation = 'horizontal')
        
        intens_tz = Slider(min=0, max = 255, value = 0, step = 1, orientation = 'vertical')
        self.btn_luz_traz = Button(text = 'OFF', background_color = red)
        lb_luz_traz = Label(text = 'Controle da Luz Trazeira', font_size = fonte)
        frame1.add_widget(lb_luz_traz)
        frame1.add_widget(self.btn_luz_traz)
        frame1.add_widget(intens_tz)
        intens_tz.bind(value=self.OnSliderValueChange_t)
        
        frame2 = BoxLayout(orientation = 'horizontal')
        
        velocidade = Slider(min=0, max = 255, value = 0, step = 1, orientation = 'vertical')
        self.btn_motor = Button(text = 'OFF', background_color = red)
        lb_motor = Label(text = 'Controle do Motor', font_size = fonte)
        self.btn_sentido = Button(text = 'Frente', background_color= yellow, on_release = self.controlasentido )
        frame2.add_widget(lb_motor)
        frame2.add_widget(self.btn_motor)
        frame2.add_widget(velocidade)
        frame2.add_widget(self.btn_sentido)
        velocidade.bind(value=self.OnSliderValueChange_m)
        
        frame3 = BoxLayout(orientation = 'horizontal')
        
        btn_sair = Button(text = 'Sair', background_color= orange, on_release = self.sair )
        frame3.add_widget(btn_sair)
        
        tela.add_widget(frame0)
        tela.add_widget(frame1)
        tela.add_widget(frame2)
        tela.add_widget(frame3)
        return tela
    
    def aciona(self):
        if(self.intensidade_m > 0): 
            self.btn_motor.text = 'ON'
            self.btn_motor.background_color = green
            self.envia_valor('m', self.intensidade_m ,self.sentido)
        else:
            self.btn_motor.text = 'OFF'
            self.btn_motor.background_color = red
            self.envia_valor('m', self.intensidade_m ,self.sentido)
        
        if(self.intensidade_f > 0):
            self.btn_luz_frente.text = 'ON'
            self.btn_luz_frente.background_color = green
            self.envia_valor('f', self.intensidade_f ,False)
        else:
            self.btn_luz_frente.text = 'OFF'
            self.btn_luz_frente.background_color = red
            self.envia_valor('f', self.intensidade_f ,False)
            
        if(self.intensidade_t > 0):
            self.btn_luz_traz.text = 'ON'
            self.btn_luz_traz.background_color = green
            self.envia_valor('t', self.intensidade_t ,False)
        else: 
            self.btn_luz_traz.text = 'OFF'
            self.btn_luz_traz.background_color = red
            self.envia_valor('t', self.intensidade_t ,False)
            
    def controlasentido(self, event):
        self.sentido = not self.sentido
        if(self.sentido == True):
            self.btn_sentido.text = 'Traz'
        else:
            self.btn_sentido.text = 'Frente'
            
    
    def envia_valor(self,item, pwm, xsentido):
        print 'Altera o valor de: %s para: %s no sentido: %s' %(item, str(pwm),xsentido)
        
    def sair(self, event):
        App.get_running_app().stop()

if __name__ in ('__android__', '__main__'):
    Main().run()