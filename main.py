from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton, MDRectangleFlatButton
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.dialog import MDDialog
import datetime
from kivymd.uix.snackbar import Snackbar
from kivy.core.window import Window

kv='''
ScreenManager:
	MainScreen:
		BoxLayout:
			AnchorLayout:
				anchor_y:'top'
				MDToolbar:
					title: 'D.O.B Calculator'
					#background_color: app.theme_cls.primary_dark
					#pos_hint:{'center_x':0.5,'center_y':0.9}
			
<MainScreen>:
	name:'mains'

	MDTextField:
		id:yob
		hint_text:'year'
		text:''
		input_filter:'float'
		size_hint_x:0.2
		max_text_length:4
		pos_hint:{'center_x':0.2,'center_y':0.7}
		
		
	MDTextField:
		id:mob
		hint_text:'month'
		text:''
		input_filter:'float'
		size_hint_x:0.2
		max_text_length:2
		pos_hint:{'center_x':0.5,'center_y':0.7}
		
		
	MDTextField:
		id:dob
		hint_text:'date'
		text:''
		input_filter:'float'
		size_hint_x:0.2
		max_text_length:2
		pos_hint:{'center_x':0.8,'center_y':0.7}	
		
	
	MDRectangleFlatButton:
		id:get
		text:'Get D.O.B'
		pos_hint:{'center_x':0.5,'center_y':0.5}
		on_release:
			root.show_dob()
		
'''

class MainScreen(Screen):

	
	def show_dob(self):
		try:
		
			self.today=datetime.date.today()
			self.today_year=self.today.year
			self.today_month=self.today.month
			self.today_date=self.today.day
			
			self.yob=self.ids.yob.text
			self.mob=self.ids.mob.text
			self.dob=self.ids.dob.text
			
			self.total_year=int(self.today_year)-int(self.yob)
			self.total_month=int(self.today_month)- int(self.mob)
			self.total_day=int(self.today_date)-int(self.dob)
				
			dialog_text='Age in years: '+str(self.total_year)+'\n'+'Total Month: '+str(self.total_month)+'\n'+'Total Days: '+str(self.total_day)
	
			dialoag=MDDialog(title='D.O.B Calculator', text=str(dialog_text), size_hint=(0.8,0.5)).open()
			
		except:
			s=Snackbar(text='Please fill the Entries First !').show()
			
sm=ScreenManager()
sm.add_widget(MainScreen(name='mains'))

class MyApp(MDApp):
	def build(self):
		
		script=Builder.load_string(kv)
		return script
	
	
MyApp().run()

