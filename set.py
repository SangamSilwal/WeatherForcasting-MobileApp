from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.image import Image
from kivymd.uix.screenmanager import ScreenManager
from test_weather import get_weather_data

KV = '''
ScreenManager:
    MainScreen:
    DeveloperScreen:

<MainScreen>:
    name: "main"
    MDBoxLayout:
        orientation: "vertical"
        spacing: dp(20)
        padding: dp(20)

        MDLabel:
            text: "Enter The Name of City"
            halign: "center"
            theme_text_color: "Primary"

        MDTextField:
            id: district_input
            hint_text: "Enter District"
            mode: "rectangle"

        MDRaisedButton:
            text: "Forecast Weather"
            pos_hint: {"center_x": 0.5}
            on_release: app.check_weather_status()

        MDLabel:
            id: result_label
            text: ""
            halign: "center"
            theme_text_color: "Secondary"

        MDRaisedButton:
            text: "Meet the Developer"
            pos_hint: {"center_x": 0.5}
            on_release: app.change_screen("developer")


<DeveloperScreen>:
    name: "developer"
    md_bg_color: 0, 0, 0, 1 
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(20)

        MDLabel:
            text: "Developer"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1,1,1,1

        MDLabel:
            text: "Howdy I am Sangam Silwal a passionate python developer"
            halign: "center"
            theme_text_color: "Custom"
            text_color : 1,1,1,1

        MDCard:
            size_hint: None, None
            size: "250dp", "250dp"
            radius: [125]
            elevation: 10
            pos_hint: {"center_x": 0.5}

            

            Image:
                source: "dev.jpg"
                size_hint: None, None
                size: "250dp", "250dp"
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                canvas.before:
                    Ellipse:
                        pos: self.pos
                        size: self.size

        MDRaisedButton:
            text: "Go Back"
            pos_hint: {"center_x": 0.5}
            on_release: app.change_screen("main")

'''
class MainScreen(MDScreen):
    pass

class DeveloperScreen(MDScreen):
    pass
class WeatherApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
    def change_screen(self,screen_name):
        self.root.current = screen_name

    def check_weather_status(self):
        city_name = self.root.get_screen("main").ids.get('district_input',None)
        if city_name:
            city_name = city_name.text.strip()

        
            if(isinstance(city_name,str) and city_name):
                try:
                    temp_dict = get_weather_data(city_name=city_name)
                    if temp_dict:

                        weather_name = str(temp_dict["name"])
                        weather_status = str(temp_dict["Weather_Status"])
                        weather_temp = str(temp_dict["feels_like"])
                        weather_min = str(temp_dict["temp_min"])
                        weather_max = str(temp_dict["temp_max"])
                        weather_pressure = str(temp_dict["pressure"])

                        weather_info = f"City:  {weather_name}\n"
                        weather_info += f"Feels Like:  {weather_temp}°F\n"
                        weather_info += f"Weather Status:  {weather_status}\n"
                        weather_info += f"Minimum Temp:  {weather_min}°F\n"
                        weather_info += f"Maximum Temp:  {weather_max}°F\n"
                        weather_info += f"Presurre:  {weather_pressure} Pascal\n"
                    


                        self.root.get_screen("main").ids.result_label.text = weather_info
                    else:
                        self.root.get_screen("main").ids.result_label.text = "Weather Data not Found"
                except Exception as e:
                    self.root.get_screen("main").ids.result_label.text = f"Sorry Getting Error: {e}"

        else:
            self.root.get_screen("main").ids.result_label.text="error in Displaying"
      






WeatherApp().run()
