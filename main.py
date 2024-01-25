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
        
        # Adicionando o título "Escolha o Treino" na terceira página
        workouts_title_text = 'Escolha o Treino'
        workouts_title = Label(text=workouts_title_text, font_size=25, size_hint_y=None, height=50)
        workouts_layout.add_widget(workouts_title)

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
        
        # Mapeamento de exercícios para cada treino e opção
        exercises_map = {
            ('inferior', 'A'): ["Mobilidade Curvado de Pé (3x12)", "Cadeira Flexora (3x15)", "Elevação Pélvica na Máquina ( 3x15)", "Cadeira Abdutora (3x15)", "Stiff (3x12)", "Panturrilheira (3x15)", "Esteira (15 minutos)"],
            ('inferior', 'B'): ["Mobilidade Posterior Segurando com a Ponta do Tênis (3x12)", "Flexora Deitada (mesa) (3x15)", "Cadeira Abdutora (3x15)", "Leg Extensor (3x15)", "Panturrilheira (3x15)", "Esteira ou Bicicleta (15 minutos)"],
            ('inferior', 'C'): ["Mobilidade de Tornozelo Solo (3x15)", "Agachamento Barra Hexagonal", "Pernada com Apoio ao Banco (3x12)", "Leg Extensor(3x15)", "Panturrilheira (3x15)", "Esteira ou Elíptico (15 minutos)"],
            ('inferior', 'D'): ["Mobilidade Posterior Segurando com a Ponta do Tênis (3x12)", "Elevação Pelve Máquina (4x1)", "Cadeira Adutora (3x15)", "Leg Press (3x15)", "Leg 45° Maquina (3x15)", "Abdominal Infra Máquina (3x12)", "Esteira ou Elíptico (15 minutos)"],
            ('superior', 'A'): ["Mobilidade Rotação de Ombro com Superband (3x12)", "Supino Reto (3x15)", "Rosca Direta ( 3x15)", "Remada Curvada (3x15)", "Tríceps Pulley (3x12)", "Abdominal Supra (3x15)", "Esteira (15 min)"],
            ('superior', 'B'): ["Mobilidade Escapular", "Supino Reto Articulado (3x12)", "Voador (3x15)", "Elevação lateral com Halter (3x12)", "Triceps Corda (+ Tríceps Testa com Corda) (3x10 cada uma)", "Triceps Francês com Halter", "Esteira ou Escada ( 15 minutos)"],
            ('superior', 'C'): ["Mobilidade Ombro no banco (Dinâmico ou Isométrico) (3x12)", "Remada Fechada (3x15)", "Rosca Direta ( 3x15)", "Supino (3x12)", "Elevação Frontal (3x15)", "Esteira (15 minutos)"],
            ('superior', 'D'): ["Mobilidade Escapular(3x12)", "Puxador Frontal (3x12)", "Crucifixo (3x12)", "Tríceps Paralela (3x12)", "Rosca Martelo (+ Rosca Direta) (3x10 each)", "Abdominal Máquina (3x12)", "Esteira (15 minutos)"]
        }

        # Adicionando o título específico do treino selecionado
        specific_title = Label(text=f"Lista de Exercícios para o Treino {treino} - Opção {option.upper()}", font_size=25, size_hint_y=None, height=50)
        exercises_layout.add_widget(specific_title)

        # Adicionando os exercícios correspondentes ao treino e opção selecionados
        for exercise in exercises_map[(option, treino)]:
            exercise_label = Label(text=exercise)
            exercises_layout.add_widget(exercise_label)

        # Atualizando o layout
        self.update_layout(exercises_layout)

    def update_layout(self, new_layout):
        # Removendo antigos widgets e adicionando novos à layout
        self.root.clear_widgets()
        self.root.add_widget(new_layout)

if __name__ == '__main__':
    MyApp().run()
