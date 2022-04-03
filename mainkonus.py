# импорт главного модуля
from kivy.app import App
# импорт модуля кнопки
from kivy.uix.button import Button
# импорт модуля ярлыка
from kivy.uix.label import Label
# импорт модуля слоя AnchorLayout
from kivy.uix.anchorlayout import AnchorLayout
# импорт модуля слоя GridLayout
from kivy.uix.gridlayout import GridLayout
# импорт модуля ввода текста
from kivy.uix.textinput import TextInput
# импорт модуля связанного с отображением окон
from kivy.core.window import Window
# для работы с FloatLayout в первую очередь
# Вы должны импортировать его
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.togglebutton import ToggleButton
# Импорт ObjectPropert для создания ссылок на объекты
from kivy.properties import ObjectProperty
# подключение экранной клавиатуры смартфона
from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemanddock')

# задаем размер окна пропорционально дисплею устройства
Window.size = (270, 540)



# создаем класс Container, унаследованный от класса AnchorLayout
class Container(AnchorLayout):

    tgb_dlina = (ObjectProperty)
    tgb_ugol = (ObjectProperty)
    tgb_m_diam = (ObjectProperty)
    tgb_b_diam = (ObjectProperty)
    lbl_dlina = (ObjectProperty)
    txtinp_dlina = (ObjectProperty)
    lbl_ugol = (ObjectProperty)
    txtinp_ugol = (ObjectProperty)
    lbl_m_diam = (ObjectProperty)
    txtinp_m_diam = (ObjectProperty)
    lbl_b_diam = (ObjectProperty)
    txtinp_b_diam = (ObjectProperty)
    txt_sprav_info = (ObjectProperty)
    btn_calculate = (ObjectProperty)

    def change_text(self):
        self.txt_sprav_info.text = "Справка"


    def calculate_dlina(self):
        import math
        try:
            self.txt_sprav_info.text = ""
            raznica_diametrov = (float(self.txtinp_b_diam.text) - float(self.txtinp_m_diam.text))
            angle_In_Radians = math.radians(float(self.txtinp_ugol.text))
            tangens_ugla_in_radiana = math.tan(angle_In_Radians)
            L = raznica_diametrov / (2 * tangens_ugla_in_radiana)
            l_result_okruglenie = round(L, 2)
            self.txtinp_dlina.text = str(l_result_okruglenie)
            self.txt_sprav_info.text = "Длина конуса равняется " + (self.txtinp_dlina.text) + " условных единиц (" \
                                                                                              "обычно указывают в мм)."
            if l_result_okruglenie < 0:
                self.txt_sprav_info.text = "У Вас получился отрицательный результат. Проверьте все данные, " \
                                           "убедитесь, что малый диаметр не превышает большой. Возможно, указанный " \
                                           "угол слишком " \
                                           "велик."
        except:
            self.txt_sprav_info.text = "Ошибка расчета. Убедитесь, что все данные указаны верно. Исправьте " \
                                       "значение и снова нажмите на кнопку с искомой величиной."

    def calculate_ugol(self):
        import math
        try:
            self.txt_sprav_info.text = ""
            raznica_diametrov = (float(self.txtinp_b_diam.text) - float(self.txtinp_m_diam.text))
            arct_ugla_alpha = (raznica_diametrov / (2 * float(self.txtinp_dlina.text)))
            arctan_alpha = math.atan(arct_ugla_alpha)
            perevod_in_gradus = math.degrees(arctan_alpha)
            alfa_result_okruglenie = round(perevod_in_gradus, 2)
            full_alfa_result_okruglenie = alfa_result_okruglenie * 2
            self.txtinp_ugol.text = str(alfa_result_okruglenie)
            self.txt_sprav_info.text = "Резцодержатель необходимо повернуть на " \
                                       "" + (self.txtinp_ugol.text) + "" \
                                       " градуса." + " Полный угол конуса будет " \
                                                     "составлять " + (str(full_alfa_result_okruglenie)) + " градуса."
            if alfa_result_okruglenie < 0:
                self.txt_sprav_info.text = "У Вас получился отрицательный результат. Проверьте все данные, " \
                                           "убедитесь, что малый диаметр не превышает большой. Возможно, указана" \
                                           " слишком большая длина."
        except:
            self.txt_sprav_info.text = "Ошибка расчета. Убедитесь, что все данные указаны верно. Исправьте " \
                                       "значение и снова нажмите на кнопку с искомой величиной."

    def calculate_m_diam(self):
        import math
        try:
            self.txt_sprav_info.text = ""
            angle_In_Radians = math.radians(float(self.txtinp_ugol.text))
            tangens_ugla_in_radiana = math.tan(angle_In_Radians)
            d = float(self.txtinp_b_diam.text) - (2 * tangens_ugla_in_radiana * float(self.txtinp_dlina.text))
            result_okruglenie = round(d, 2)
            self.txtinp_m_diam.text = str(result_okruglenie)
            self.txt_sprav_info.text = "Малый диаметр равен " + (self.txtinp_m_diam.text) + " условных единиц " \
                                                                                            "(обычно указывают в мм)."
        except:
            self.txt_sprav_info.text = "Ошибка расчета. Убедитесь, что все данные указаны верно. Исправьте " \
                                       "значение и снова нажмите на кнопку с искомой величиной."


# создаем класс MyApp, унаследованный от класса App. Основной класс, ответственный за запуск приложения.
class MyApp(App):
    def build(self):
        self.title = 'Помощник токаря'
        # в функции возвращаем значение класса Container
        return Container()


# проверка, что запускаем методом .run сам файлик mainkonus.py, а не из другого файла путем импорта. Метод .run прописан
# в классе App
if __name__ == '__main__':
    MyApp().run()
