import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

wintext = Label(text="", font_size=100)

box = BoxLayout(orientation='vertical')

flag = True
win = ""
popup = Popup(title="Congratulations",
content=box, auto_dismiss=True)

class TicTacToe(Widget):
	b1 = ObjectProperty(None)
	b2 = ObjectProperty(None)
	b3 = ObjectProperty(None)
	b4 = ObjectProperty(None)
	b5 = ObjectProperty(None)
	b6 = ObjectProperty(None)
	b7 = ObjectProperty(None)
	b8 = ObjectProperty(None)
	b9 = ObjectProperty(None)

	def btn(self, instance):
		global flag
		if flag==True and instance. text=="0":
			instance.text = "o"
			flag = False
		elif flag==False and instance.text=="0":
			instance.text = "×"
			flag = True
		self.check()
		
	def check(self):
		global win
		if self.b1.text == self.b2.text and self.b1.text==self.b3.text and self.b1.text!="0":
			self.b1.background_color = (1,0,0,1)
			self.b2.background_color = (1,0,0,1)
			self.b3.background_color = (1,0,0,1)
			self.b1.disabled = True
			self.b2.disabled = True
			self.b3.disabled = True
			if self.b1.text == "o":
				win = 1
			else:
				win = 2
			self.getwin()
			
		elif self.b4.text == self.b5.text and self.b5.text==self.b6.text and self.b5.text!="0":
			self.b4.background_color = (1,0,0,1)
			self.b5.background_color = (1,0,0,1)
			self.b6.background_color = (1,0,0,1)
			self.b4.disabled = True
			self.b5.disabled = True
			self.b6.disabled = True
			if self.b4.text == "o":
				win = 1
			else:
				win = 2
			self.getwin()
			
		elif self.b7.text == self.b8.text and self.b8.text==self.b9.text and self.b8.text!="0":
			self.b7.background_color = (1,0,0,1)
			self.b8.background_color = (1,0,0,1)
			self.b9.background_color = (1,0,0,1)
			self.b7.disabled = True
			self.b8.disabled = True
			self.b9.disabled = True
			if self.b7.text == "o":
				win = 1
			else:
				win = 2
			self.getwin()
			
		elif self.b1.text == self.b4.text and self.b4.text==self.b7.text and self.b1.text!="0":
			self.b1.background_color = (1,0,0,1)
			self.b4.background_color = (1,0,0,1)
			self.b7.background_color = (1,0,0,1)
			self.b1.disabled = True
			self.b4.disabled = True
			self.b7.disabled = True
			if self.b4.text == "o":
				win = 1
			else:
				win = 2
			self.getwin()
			
		elif self.b2.text == self.b5.text and self.b5.text==self.b8.text and self.b2.text!="0":
			self.b2.background_color = (1,0,0,1)
			self.b5.background_color = (1,0,0,1)
			self.b8.background_color = (1,0,0,1)
			self.b2.disabled = True
			self.b5.disabled = True
			self.b8.disabled = True
			if self.b5.text == "o":
				win = 1
			else:
				win = 2
			self.getwin()
			
		elif self.b3.text == self.b6.text and self.b6.text==self.b9.text and self.b3.text!="0":
			self.b3.background_color = (1,0,0,1)
			self.b6.background_color = (1,0,0,1)
			self.b9.background_color = (1,0,0,1)
			self.b3.disabled = True
			self.b6.disabled = True
			self.b9.disabled = True
			if self.b3.text == "o":
				win = 1
			else:
				win = 2
			self.getwin()
			
		elif self.b1.text == self.b5.text and self.b5.text==self.b9.text and self.b1.text!="0":
			self.b1.background_color = (1,0,0,1)
			self.b5.background_color = (1,0,0,1)
			self.b9.background_color = (1,0,0,1)
			self.b1.disabled = True
			self.b5.disabled = True
			self.b9.disabled = True
			if self.b5.text == "o":
				win = 1
			else:
				win = 2
			self.getwin()
			
		elif self.b3.text == self.b5.text and self.b5.text==self.b7.text and self.b3.text!="0":
			self.b3.background_color = (1,0,0,1)
			self.b5.background_color = (1,0,0,1)
			self.b7.background_color = (1,0,0,1)
			self.b3.disabled = True
			self.b5.disabled = True
			self.b7.disabled = True
			if self.b5.text == "o":
				win = 1
			else:
				win = 2
			self.getwin()
			
		elif self.b1.text!="0" and self.b2.text!="0" and self.b3.text!="0" and self.b4.text!="0" and self.b5.text!="0" and self.b6.text!="0" and self.b7.text!="0" and self.b8.text!="0" and self.b9.text!="0":
			win = "Tie"
			self.getwin()		
	
	def getwin(self):
		global win
		if win == 1:
			wintext.text = "Player 1 Wins!"
		elif win==2:
			wintext.text = "Player 2 Wins!"
		else:
			wintext.text = "It's A Tie!"
				
		box.add_widget(wintext)
		popup.open()
					
class MyApp(App):
	def build(self):
		return TicTacToe()
		
if __name__=="__main__":
	MyApp().run()
