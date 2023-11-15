from manim import *
import random
import numpy as np
from dicegpt import *
class MeanVarianceStd_scene_3(Scene):
    def construct(self):
        
        
        face1 = Face1().scale(0.2)
        face2 = Face2().scale(0.2)
        face3 = Face3().scale(0.2)
        face4 = Face4().scale(0.2)
        face5 = Face5().scale(0.2)
        face6 = Face6().scale(0.2)
        
        num_data_sets = 15
        probability_data = self.generate_random_probability_data(num_data_sets)
        
        # Create initial chart
        chart = self.create_bar_chart(probability_data[0])
        self.play(Create(chart), runtime=2, smooth=True)

        faces = [face1, face2, face3, face4, face5, face6]
        for i, face in enumerate(faces):
            face.next_to(chart.get_x_axis().n2p(i + 0.5), DOWN, buff=0.15)
        self.add(*faces)
        
        
        # Calculate initial mean and std
        mean, std = self.calculate_mean_and_std(probability_data[0])

        # Create mean and std lines
        mean_line = self.create_line(chart, mean, PINK)
        mu = MathTex(r"\mu=" + str(round(mean,2))).shift(UP*2,RIGHT*4).set_color(PINK)
        std_line_left = self.create_line(chart, mean - std, RED)
        std_line_right = self.create_line(chart, mean + std, RED)
        sigma=MathTex(r"\sigma=" + str(round(std,2))).next_to(mu, DOWN).set_color(RED)
        
        
        # Create initial arrows and labels
        arrow_left = Arrow(mean_line.get_start(), std_line_left.get_start(), buff=0.2).set_color(RED).shift(UP*2)
        arrow_right = Arrow(mean_line.get_start(), std_line_right.get_start(), buff=0.2).set_color(RED).shift(UP*2)
        sigma_left_label = MathTex(r"\sigma").next_to(arrow_left, UP).set_color(RED)
        sigma_right_label = MathTex(r"\sigma").next_to(arrow_right, UP).set_color(RED)

        # Add lines and labels to scene
        self.add(mean_line, std_line_left, std_line_right, sigma,  mu,arrow_left, arrow_right, sigma_left_label, sigma_right_label)

        # Update chart, lines, and labels for each new data set
        for prob_data in probability_data[1:]:
            new_chart = self.create_bar_chart(prob_data)
            mean, std = self.calculate_mean_and_std(prob_data)
            new_mean_line = self.create_line(new_chart, mean, PINK)
            new_mu = MathTex(r"\mu=" + str(round(mean,2))).shift(UP*2,RIGHT*4).set_color(PINK)
            new_std_line_left = self.create_line(new_chart, mean - std, RED)
            new_std_line_right = self.create_line(new_chart, mean + std, RED)
            new_sigma=MathTex(r"\sigma=" + str(round(std,2))).next_to(new_mu, DOWN).set_color(RED)
            new_arrow_left = Arrow(new_mean_line.get_start(), new_std_line_left.get_start(), buff=0.2).set_color(RED).shift(UP*2)
            new_arrow_right = Arrow(new_mean_line.get_start(), new_std_line_right.get_start(), buff=0.2).set_color(RED).shift(UP*2)
            new_sigma_left_label = MathTex(r"\sigma").next_to(new_arrow_left, UP).set_color(RED)
            new_sigma_right_label = MathTex(r"\sigma").next_to(new_arrow_right, UP).set_color(RED)


            self.play(
                Transform(chart, new_chart),
                Transform(mean_line, new_mean_line),
                Transform(mu, new_mu),
                Transform(std_line_left, new_std_line_left),
                Transform(std_line_right, new_std_line_right),
                Transform(sigma, new_sigma),
                Transform(arrow_left, new_arrow_left),
                Transform(arrow_right, new_arrow_right),
                Transform(sigma_left_label, new_sigma_left_label),
                Transform(sigma_right_label, new_sigma_right_label),
                        
                run_time=1,smooth=True
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
        return BarChart(
            values=probability_data,
            y_range=[0, 0.5, 0.1],
            x_length=6,
            y_length=5,
            bar_colors=[BLUE_A, BLUE_B, BLUE_C, BLUE_D, BLUE_E, TEAL_E],
            bar_width=1,
            bar_fill_opacity=1,
            bar_stroke_width=0,
        )

    def calculate_mean_and_std(self, probability_data):
        mean = sum((i + 1) * p for i, p in enumerate(probability_data))
        var = sum((i + 1 - mean) ** 2 * p for i, p in enumerate(probability_data))
        std = np.sqrt(var)
        return mean, std

    def create_line(self, chart, x_value, color):
        return Line(
            start=chart.get_x_axis().n2p(x_value),
            end=[chart.get_x_axis().n2p(x_value)[0], chart.get_y_axis().n2p(0.3)[1], 0],
            color=color
        )