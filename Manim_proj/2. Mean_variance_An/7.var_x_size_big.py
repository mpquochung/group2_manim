from manim import *
class Var_x_size_big(Scene):
    def construct(self):
        prob_x = [  0.4,
                    0.25,
                    0.15,
                    0.1,
                    0.07,
                    0.03]
        
        self.value_x=[1,2,3,4,5,6]
        chart_x=self.create_bar_chart_x(prob_x)
        mean_x=self.calculate_mean(prob_x)
        std_left_x, std_right_x = self.calculate_std_interval(prob_x)
        mean_line_x = self.mean_line(chart_x, mean_x)
        mean_line_std_left_x = self.mean_line(chart_x, std_left_x)
        mean_line_std_right_x = self.mean_line(chart_x, std_right_x)
        arrow_left, arrow_right = self.get_mean_std_arrows(chart_x, mean_x, std_left_x, std_right_x)

        prob_x_1 = {1:0.4,
                    2: 0.25,
                    3: 0.15,
                    4: 0.1,
                    5: 0.07,
                    6: 0.03}
        
        result_x_n=self.dice_sum(prob_x_1, 7)
        prob_x_n=list(result_x_n.values())
        self.value_x_n=list(result_x_n.keys())
        chart_x_n=self.create_bar_chart_x_n(prob_x_n)
        chart_x_n.shift(DOWN*2,LEFT*1)
        
        group_chart_x=VGroup(chart_x,mean_line_x,mean_line_std_left_x,mean_line_std_right_x,arrow_left,arrow_right)
        group_chart_x.scale(0.25)
        group_chart_x.shift(UP*2.5,LEFT*5)
        text1=MathTex("X_1")
        text1.shift(UP*3,LEFT*4.5)
        text1.set_color(BLUE)
        text1.scale(0.5)
        
        
        group_chart_x_1=group_chart_x.copy()
        group_chart_x_1.next_to(group_chart_x,RIGHT*2)
        text2=MathTex("X_2")
        text2.shift(UP*3,LEFT*1.5)
        text2.set_color(BLUE)
        text2.scale(0.5)
        
        group_chart_x_2=group_chart_x.copy()
        group_chart_x_2.next_to(group_chart_x_1,RIGHT*2)
        text3=MathTex("X_3")
        text3.shift(UP*3,RIGHT*2)
        text3.set_color(BLUE)
        text3.scale(0.5)
        
        
        d1=Dot(color=WHITE)
        d1.next_to(group_chart_x_2)
        d2=Dot(color=WHITE)
        d2.next_to(d1)
        d3=Dot(color=WHITE)
        d3.next_to(d2)
        
        
        group_chart_x_3=group_chart_x.copy()
        group_chart_x_3.next_to(d3)
        text4=MathTex("X_n")
        text4.shift(UP*3,RIGHT*6)
        text4.set_color(BLUE)
        text4.scale(0.5)
        
        line = Line(np.array([-20, 1, 0]), np.array([20, 1, 0]))
        text_group_1=VGroup(text1,text2,text3,text4)
        
        text_group=MathTex("X_1+X_2+X_3+...+X_n")
        text_group.set_color(BLUE)
        text_group.shift(LEFT*3)
        
        text_group_ct=MathTex(
            "\sigma^2_{X_1+...+X_n}",
            "=",
            "n.",
            "\sigma^2_{X_1}"
        )
        text_group_ct[0].shift(RIGHT*3)
        text_group_ct[1].next_to(text_group_ct[0],RIGHT*2)
        text_group_ct[2].next_to(text_group_ct[1],RIGHT*2)
        text_group_ct[3].next_to(text_group_ct[2])
        text_group_ct_gr=VGroup(text_group_ct[0],text_group_ct[1],text_group_ct[2],text_group_ct[3])
        
        
        var_group_ct=MathTex("Var(X_1+...+X_n)","Var(X_1)")
        var_group_ct.scale(0.5)
        var_group_ct[0].next_to(text_group_ct[0],DOWN*2)
        var_group_ct[1].next_to(text_group_ct[3],DOWN*2)
        framebox1=SurroundingRectangle(text_group_ct[0],buff=0.1)
        framebox2=SurroundingRectangle(text_group_ct[3],buff=0.1)
        
        var_ct_sqrt=MathTex("\sigma_{X_1+...+X_n}=\sqrt n . \sigma_{X_1}")
        
        var_ct_sqrt.next_to(text_group_ct_gr,DOWN*2)
        #self.add(var_ct_sqrt)
        
        #self.add(text_group_ct[0],text_group_ct[1],text_group_ct[2],text_group_ct[3])
        #self.play(FadeOut(framebox1),FadeOut(framebox2),
        #FadeOut(var_group_ct[0]),FadeOut(var_group_ct[1]))
        
        
        self.add(text1,text2,text3,text4,
            group_chart_x,
                 group_chart_x_1,
                 group_chart_x_2,
                 d1,
                 d2,
                 d3,
                 group_chart_x_3,
                 line)
        
        self.play(ReplacementTransform(group_chart_x.copy(),chart_x_n),
                  ReplacementTransform(group_chart_x_1.copy(),chart_x_n),
                    ReplacementTransform(group_chart_x_2.copy(),chart_x_n),
                    ReplacementTransform(group_chart_x_3.copy(),chart_x_n),
                ReplacementTransform(text_group_1.copy(),text_group),
                  runtime=5)
        self.play(ReplacementTransform(text_group.copy(),text_group_ct[0]),
                  ReplacementTransform(text_group.copy(),text_group_ct[1]),
                  ReplacementTransform(text_group.copy(),text_group_ct[2]),
                    ReplacementTransform(text_group.copy(),text_group_ct[3]),runtime=2)
        self.play(Create(framebox1), Create(framebox2),Create(var_group_ct[0]),Create(var_group_ct[1]),runtime=2)
        self.wait(2)
        self.play(FadeOut(framebox1),FadeOut(framebox2),
        FadeOut(var_group_ct[0]),FadeOut(var_group_ct[1]))
        
        self.play(ReplacementTransform(text_group_ct_gr.copy(),var_ct_sqrt),runtime=2)
        
        self.wait(2)



    def create_bar_chart_x(self, probability_data):
        chart = BarChart(
                values=probability_data,
                bar_names=self.value_x,
                bar_colors=[
          interpolate_color(BLUE, GREEN, x/len(self.value_x)) 
          for x in range(len(self.value_x))],
                y_range=[0, 0.5,0.1],
                x_length=10,
                y_length=5,
                bar_width=1,
                bar_fill_opacity=1,
                bar_stroke_width=0,
            )
        
        return chart
    
    
    def create_bar_chart_x_n(self, probability_data):
        chart = BarChart(
                values=probability_data,
                bar_colors=[
          interpolate_color(BLUE, GREEN, x/len(self.value_x_n)) 
          for x in range(len(self.value_x_n))],
                y_range=[0, 0.2,0.1],
                x_length=10,
                y_length=3,
                bar_width=1,
                bar_fill_opacity=0.7,
                bar_stroke_width=0.2,
            )
        
        return chart
    
    def calculate_mean(self, probability_data):
        mean_data = sum((i + 1) * p for i, p in enumerate(probability_data))
        return mean_data
    
    def calculate_std_interval(self, probability_data):
        mean_data = self.calculate_mean(probability_data)
        var_data = sum((i + 1) ** 2 * p for i, p in enumerate(probability_data)) - mean_data ** 2
        std_data = var_data ** 0.5
        std_data_left = mean_data - std_data
        std_data_right = mean_data + std_data
        return std_data_left, std_data_right

    
    def mean_line(self, chart, mean_data):
        max_prob = max(chart.values)
        mean_line = Line(
            start=chart.get_x_axis().n2p(mean_data),
            end=[chart.get_x_axis().n2p(mean_data)[0], chart.get_y_axis().n2p(max_prob*1.2)[1], 0],
            color=LIGHTER_GREY,stroke_opacity=0.5
        )
        return mean_line
    
    def get_mean_std_arrows(self,chart, mean, std_left, std_right, arrow_color=WHITE):

        start = chart.get_x_axis().n2p(mean)
        end_left = chart.get_x_axis().n2p(std_left)
        end_right = chart.get_x_axis().n2p(std_right)

        arrow_left = Arrow(start=start, end=end_left, color=arrow_color)
        arrow_left.shift(UP*4)
        arrow_right = Arrow(start=start, end=end_right, color=arrow_color)
        arrow_right.shift(UP*4)
         
        
        return arrow_left, arrow_right
    
    def dice_sum(self,prob, n):
        if n == 1:
            return prob
        else:
            result = {}
            for i in range(1, 7):
                for j in self.dice_sum(prob, n - 1).items():
                    result[i + j[0]] = result.get(i + j[0], 0) + prob[i] * j[1]
            for i in range(1, min(result.keys())):
                if i not in result.keys():
                    result[i]=0
            sorted_result = dict(sorted(result.items()))
            return sorted_result
            