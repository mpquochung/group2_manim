from manim import *
from dicegpt import *
import random

class MeanScene(Scene):
    def construct(self):
        num_data_sets = 20  # So luong bo du lieu xac suat
        probability_data = self.generate_random_probability_data(num_data_sets)
        
        face1 = Face1()
        face2 = Face2()
        face3 = Face3()
        face4 = Face4()
        face5 = Face5()
        face6 = Face6()

        # Text, MathTex
        text = Tex("Mean", color=WHITE)
        
        
        # Tao bieu do ban dau
        chart = self.create_bar_chart(probability_data[0])
        self.play(Create(chart), runtime=2, smooth=True)
        self.wait(0)

        face1.scale(0.2)
        face2.scale(0.2)
        face3.scale(0.2)
        face4.scale(0.2)
        face5.scale(0.2)
        face6.scale(0.2)

        faces = [face1, face2, face3, face4, face5, face6]
        for i, face in enumerate(faces):
            face.next_to(chart.get_x_axis().n2p(i + 0.5), DOWN, buff=0.15)
        self.add(*faces)

        mean_data_ct = self.calculate_mean(probability_data[0])
       
        mean_line = Line(
            start=chart.get_x_axis().n2p(mean_data_ct),
            end=[chart.get_x_axis().n2p(mean_data_ct)[0], chart.get_y_axis().n2p(0.3)[1], 0],
            color=PINK
        )
        mu = MathTex(r"\mu=" + str(round(mean_data_ct,2))).next_to(mean_line, UP)
        # Calculate the shift vector
        shift_vector = mean_line.get_center() - text.get_center()

            # Shift the text
        text.shift(shift_vector, UP*3, LEFT*1)
        
        

       
        self.add(mean_line,text,mu)  # Them mean line vao canh
        
        for prob_data in probability_data[1:]:
            # Calculate new mean
            new_mean = self.calculate_mean(prob_data)

            # Update mu content
            new_mu = MathTex(r"\mu=" + str(round(new_mean,2))).next_to(mean_line, UP)

            # Create new mean line
            new_mean_line = Line(
                start=chart.get_x_axis().n2p(new_mean),
                end=[chart.get_x_axis().n2p(new_mean)[0], chart.get_y_axis().n2p(0.3)[1], 0],
                color=PINK
            )

            # Group operations
            self.play(
                Transform(chart, self.create_bar_chart(prob_data)),
                Transform(mean_line, new_mean_line),
                Transform(mu, new_mu),
                smooth=True
            )
                        
            
            
            

    def generate_random_probability_data(self, num_data_sets):
        probability_data_list = []
        for _ in range(num_data_sets):
            probability_data = [random.uniform(0, 1) for _ in range(6)]
            total_probability = sum(probability_data)
            normalized_probability_data = [p / total_probability for p in probability_data]
            probability_data_list.append(normalized_probability_data)
        return probability_data_list

    def create_bar_chart(self, probability_data):
        bar_colors = [BLUE_A, BLUE_B, BLUE_C, BLUE_D, BLUE_E, TEAL_E]

        chart = BarChart(
            values=probability_data,
            y_range=[0, 0.5, 0.1],
            x_length=6,
            y_length=5,
            bar_colors=bar_colors,
            bar_width=1,
            bar_fill_opacity=1,
            bar_stroke_width=0,
        )
        return chart

    def calculate_mean(self, probability_data):
        mean_data = sum((i + 1) * p for i, p in enumerate(probability_data))
        return mean_data

    
