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
        
        # Adicionando o título "Escolha o Treino" no topo da tela
        options_title = Label(text='Escolha o Treino', font_size=25, size_hint_y=None, height=50)
        options_layout.add_widget(options_title)

        option1_button = Button(text='Opção Inferior', on_press=lambda x: self.show_workouts_page(x, 'inferior'), size_hint=(None, None))
        option2_button = Button(text='Opção Superior', on_press=lambda x: self.show_workouts_page(x, 'superior'), size_hint=(None, None))
        option1_button.size = option2_button.size = (500, 80)
        option1_button.pos_hint = {'center_x': 0.5}
        option2_button.pos_hint = {'center_x': 0.5}
        option1_button.background_color = option2_button.background_color = (0, 0.5, 0, 1)

        options_layout.add_widget(option1_button)
        options_layout.add_widget(option2_button)

        # Atualizando o layout
        self.update_layout(options_layout)

    def show_workouts_page(self, instance, option):
        # Página de Treinos
        workouts_layout = BoxLayout(orientation='vertical', spacing=30, padding=20)
        
        # Adicionando o título "Lista de Exercícios para o Treino" no topo da tela
        workouts_title = Label(text='Lista de Exercícios para o Treino', font_size=25, size_hint_y=None, height=50)
        workouts_layout.add_widget(workouts_title)
        
        workouts_label = Label(text='Escolha o Treino', font_size=25)

        # Adicionando botões para cada treino
        workouts_buttons = []
        for i in range(4):
            button = Button(text=f'Treino {chr(65 + i)}', on_press=lambda x, treino=chr(65 + i): self.show_exercises_page(x, option, treino), size_hint=(None, None))
            button.size = (500, 80)
            button.pos_hint = {'center_x': 0.5}
            button.background_color = (0, 0.5, 0, 1)
            workouts_buttons.append(button)
            workouts_layout.add_widget(button)

        # Atualizando o layout
        self.update_layout(workouts_layout)

    def show_exercises_page(self, instance, option, treino):
        # Página de Exercícios
        exercises_layout = BoxLayout(orientation='vertical', spacing=30, padding=20)
        
        # Adicionando o título "Lista de Exercícios para o Treino" no topo da tela
        exercises_title = Label(text='Lista de Exercícios para o Treino', font_size=25, size_hint_y=None, height=50)
        exercises_layout.add_widget(exercises_title)

        exercises_label = Label(text=f'Lista de Exercícios para o Treino {treino} - Opção {option.upper()}', font_size=25)

        # Mapeamento de exercícios para cada treino e opção
        exercises_map = {
            ('inferior', 'A'): ["Mobilidade Curvado de Pé (3x12)", "Cadeira flexora (3x15)", "Elevação pélvica na maquina ( 3x15)", "cadeira abdutora (3x15)", "stiff (3x12)", "Panturrilheira (3x15)", "Esteira (15 minutos)"],
            ('inferior', 'B'): ["Mobilidade posterior segurando com a ponta do tênis (3x12)", "Flexora deitada (mesa) (3x15)", "Cadeira abdutora (3x15)", "Leg extensor (3x15)", "Panturrilheira (3x15)", "Esteira ou bicicleta (15 minutos)"],
            ('inferior', 'C'): ["Mobilidade de tornozelo solo (3x15)", "Agachamento barra hexagonal", "Pernada com apoio ao banco (3x12)", "Leg extensor(3x15)", "Panturrilheira (3x15)", "Esteira ou Elíptico (15 minutos)"],
            ('inferior', 'D'): ["Mobilidade posterior segurando com a ponta do tênis (3x12)", "Elevação pelve maquina (4x1)", "Cadeira adutora (3x15)", "Leg press (3x15)", "Leg 45 maquina (3x15)", "Abdominal infra maquina (3x12)", "Esteira ou Elíptico (15 minutos)"],
            ('superior', 'A'): ["Mobilidade rotação de ombro com superband (3x12)", "Supino reto (3x15)", "Rosca direta ( 3x15)", "Remada curvada (3x15)", "Tríceps Pulley (3x12)", "Abdominal supra (3x15)", "Esteira (15 min)"],
            ('superior', 'B'): ["Mobilidade escapular", "Supino reto articulado (3x12)", "Voador (3x15)", "Elevação lateral com halter (3x12)", "Triceps corda (+tríceps testa com corda) (3x10 cada uma)", "Triceps francês com halter", "Esteira ou escada ( 15 minutos)"],
            ('superior', 'C'): ["Mobilidade ombro no banco (dinâmico ou isométrico) (3x12)", "Remada fechada (3x15)", "Rosca direta ( 3x15)", "Supino (3x12)", "Elevação frontal (3x15)", "Esteira( 15 minutos)"],
            ('superior', 'D'): ["Mobilidade escapular(3x12)", "Puxador frontal (3x12)", "Crucifixo (3x12)", "Tríceps paralela (3x12)", "Rosca martelo (+ rosca direta) (3x10 cada uma)", "Abdominal máquina (3x12)", "Esteira (15 minutos)"]
        }

        # Adicionando os exercícios correspondentes ao treino e opção selecionados
        for exercise in exercises_map[(option, treino)]:
            exercise_label = Label(text=exercise)
            exercises_layout.add_widget(exercise_label)

        # Definindo a cor do rótulo para verde escuro
        exercises_label.color = (0, 0.5, 0, 1)
        
        # Adicionando o título no topo da tela
        top_layout = BoxLayout(orientation='vertical', spacing=10)
        top_layout.add_widget(exercises_label)
        exercises_layout.add_widget(top_layout)

        # Atualizando o layout
        self.update_layout(exercises_layout)

    def update_layout(self, new_layout):
        # Removendo antigos widgets e adicionando novos à layout
        self.root.clear_widgets()
        self.root.add_widget(new_layout)

if __name__ == '__main__':
    MyApp().run()
