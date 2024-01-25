from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        self.current_layout = self.create_initial_layout()
        return self.current_layout

    def create_initial_layout(self):
        # Página Inicial
        layout = FloatLayout()

        # Substitua o caminho da imagem pelo caminho correto no seu sistema
        image_path = r'C:\Users\mylen\Downloads\treino.png'
        initial_image = Image(source=image_path, size=(800, 800), size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Adicionando opção "Continuar" abaixo da imagem
        continue_button = Button(text='Continuar', on_press=self.show_options, size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.1})
        continue_button.size = (200, 50)
        continue_button.background_color = (0, 0.5, 0, 1)  # Cor verde escuro (R, G, B, A)

        layout.add_widget(initial_image)
        layout.add_widget(continue_button)

        return layout

    def show_options(self, instance):
        # Página de Opções
        options_layout = BoxLayout(orientation='vertical', spacing=30, padding=20)
        option1_button = Button(text='Opção Posterior', on_press=self.show_workouts_page, size_hint=(None, None))
        option2_button = Button(text='Opção Inferior', on_press=self.show_workouts_page, size_hint=(None, None))
        option1_button.size = option2_button.size = (500, 80)
        option1_button.pos_hint = {'center_x': 0.5}
        option2_button.pos_hint = {'center_x': 0.5}
        option1_button.background_color = option2_button.background_color = (0, 0.5, 0, 1)

        options_layout.add_widget(option1_button)
        options_layout.add_widget(option2_button)

        # Atualizando o layout
        self.update_layout(options_layout)

    def show_workouts_page(self, instance):
        # Página de Treinos
        workouts_layout = BoxLayout(orientation='vertical', spacing=30, padding=20)
        workout_a_button = Button(text='Treino A', on_press=self.show_exercises_page_a, size_hint=(None, None))
        workout_b_button = Button(text='Treino B', on_press=self.show_exercises_page, size_hint=(None, None))
        workout_c_button = Button(text='Treino C', on_press=self.show_exercises_page, size_hint=(None, None))
        workout_d_button = Button(text='Treino D', on_press=self.show_exercises_page, size_hint=(None, None))
        workout_a_button.size = workout_b_button.size = workout_c_button.size = workout_d_button.size = (500, 80)
        workout_a_button.pos_hint = {'center_x': 0.5}
        workout_b_button.pos_hint = {'center_x': 0.5}
        workout_c_button.pos_hint = {'center_x': 0.5}
        workout_d_button.pos_hint = {'center_x': 0.5}
        workout_a_button.background_color = workout_b_button.background_color = workout_c_button.background_color = workout_d_button.background_color = (0, 0.5, 0, 1)

        workouts_layout.add_widget(workout_a_button)
        workouts_layout.add_widget(workout_b_button)
        workouts_layout.add_widget(workout_c_button)
        workouts_layout.add_widget(workout_d_button)

        # Atualizando o layout
        self.update_layout(workouts_layout)

    def show_exercises_page_a(self, instance):
        # Página de Exercícios para o Treino A
        exercises_layout = BoxLayout(orientation='vertical', spacing=30, padding=20)
        exercises_label = Label(text='Lista de Exercícios para o Treino A (posterior de coxa)', font_size=25)

        # Lista de exercícios específicos para o Treino A
        exercise_list = [
            "1. Alongamento Curvado de Pé (3x12)",
            "2. Cadeira flexora (3x15)",
            "3. Elevação pélvica na máquina (3x15)",
            "4. Cadeira abdutora (3x15)",
            "5. Stiff (3x12)",
            "6. Panturrilha na máquina (3x15)",
            "7. Esteira (15 min)"
        ]

        # Adicionando rótulo e lista de exercícios
        exercises_layout.add_widget(exercises_label)

        for exercise in exercise_list:
            exercise_label = Label(text=exercise)
            exercises_layout.add_widget(exercise_label)

        # Definindo a cor do rótulo para verde escuro
        exercises_label.color = (0, 0.5, 0, 1)

        # Atualizando o layout
        self.update_layout(exercises_layout)

    def show_exercises_page(self, instance):
        # Página de Exercícios
        exercises_layout = BoxLayout(orientation='vertical', spacing=30, padding=20)
        exercises_label = Label(text='Lista de Exercícios para o Treino selecionado', font_size=25)

        # Adicione aqui a lógica para mostrar a lista de exercícios do treino selecionado

        exercises_layout.add_widget(exercises_label)

        # Definindo a cor do rótulo para verde escuro
        exercises_label.color = (0, 0.5, 0, 1)

        # Adicionando botões com a mesma cor de fundo verde escuro
        exercise_button1 = Button(text='Exercício 1', on_press=self.on_exercise_button_press, size_hint=(None, None))
        exercise_button2 = Button(text='Exercício 2', on_press=self.on_exercise_button_press, size_hint=(None, None))
        exercise_button1.size = exercise_button2.size = (500, 80)
        exercise_button1.pos_hint = {'center_x': 0.5}
        exercise_button2.pos_hint = {'center_x': 0.5}
        exercise_button1.background_color = exercise_button2.background_color = (0, 0.5, 0, 1)

        exercises_layout.add_widget(exercise_button1)
        exercises_layout.add_widget(exercise_button2)

        # Atualizando o layout
        self.update_layout(exercises_layout)

    def on_exercise_button_press(self, instance):
        # Adicione a lógica que você deseja executar quando um botão de exercício for pressionado
        print(f'Botão de exercício pressionado: {instance.text}')

    def update_layout(self, new_layout):
        # Removendo antigos widgets e adicionando novos à layout
        self.root.clear_widgets()
        self.root.add_widget(new_layout)

if __name__ == '__main__':
    MyApp().run()
