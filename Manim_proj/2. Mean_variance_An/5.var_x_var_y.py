from manim import *
class Var_x_var_y(Scene):
    def construct(self):
        prob_x = [0.4,
                    0.25,
                    0.15,
                    0.1,
                    0.07,
                    0.03]
        prob_y=[0.0931223187824122, 0.09244363999679484, 
                0.09857109374382911, 0.07539346507634488, 
                0.12231457963118371, 0.13181563048618272,
                0.10678581304639076, 0.07560740268709486, 
                0.0841507571277572, 0.11079249161421617, 0.009002807807793412]
        self.value_x=[1,2,3,4,5,6]
        self.value_y=[1,2,3,4,5,6,7,8,9,10,11]
        
        distribution_sum_xy=self.calculate_sum_probability_distribution(self.value_x, prob_x, self.value_y, prob_y)
        for i in range(1, min(distribution_sum_xy.keys())):
                if i not in distribution_sum_xy.keys():
                    distribution_sum_xy[i]=0
        sorted_dis_sum_xy = dict(sorted(distribution_sum_xy.items()))
    
        formula=MathTex("X","Y","X+Y","Var(X+Y)","Var(",")","X","+","Y")
        text1=Text("Assuming")
        text2=Text("and")
        text3=Text("are independent")
        
        formula_1=MathTex("\sigma_{X+Y}^2=\sigma_X^2 + \sigma _Y^2")
        
        prob_xy=list(sorted_dis_sum_xy.values())
       
        self.value_xy=list(sorted_dis_sum_xy.keys())
        
        line = Line(np.array([-20, 0, 0]), np.array([20, 0, 0]))

        mean_x=self.calculate_mean(prob_x)
        mean_y=self.calculate_mean(prob_y)
        mean_xy=self.calculate_mean(prob_xy)

        std_left_x, std_right_x = self.calculate_std_interval(prob_x)
        std_left_y, std_right_y = self.calculate_std_interval(prob_y)
        std_left_xy, std_right_xy = self.calculate_std_interval(prob_xy)
        
        
        # Hiển thị đường thẳng
        self.add(line)
        
        chart_x=self.create_bar_chart_x(prob_x)
        chart_x.scale(0.5)
        chart_x.shift(UP*2,LEFT*3.5)
        mean_line_x = self.mean_line(chart_x, mean_x)
        mean_line_std_left_x = self.mean_line(chart_x, std_left_x)
        mean_line_std_right_x = self.mean_line(chart_x, std_right_x)
        
        chart_y=self.create_bar_chart_y(prob_y)
        chart_y.shift(UP*2,RIGHT*3.5)
        chart_y.scale(0.5)
        mean_line_y = self.mean_line(chart_y, mean_y)
        mean_line_std_left_y= self.mean_line(chart_y, std_left_y)
        mean_line_std_right_y = self.mean_line(chart_y, std_right_y)
        
        chart_xy=self.create_bar_chart_xy(prob_xy)
        chart_xy.shift(DOWN*2,LEFT*2.5)
        chart_xy.scale(0.5)
        mean_line_xy = self.mean_line(chart_xy, mean_xy)
        mean_line_std_left_xy= self.mean_line(chart_xy, std_left_xy)
        mean_line_std_right_xy = self.mean_line(chart_xy, std_right_xy)
        
        
        arrow_left_x, arrow_right_x = self.get_mean_std_arrows(chart_x, mean_x, std_left_x, std_right_x)
        arrow_left_y, arrow_right_y = self.get_mean_std_arrows(chart_y, mean_y, std_left_y, std_right_y)
        arrow_left_xy, arrow_right_xy = self.get_mean_std_arrows(chart_xy, mean_xy, std_left_xy, std_right_xy)
       
        group_arrow=VGroup(arrow_left_x, arrow_right_x, arrow_left_y, arrow_right_y)
        group_arrow_xy=VGroup(arrow_left_xy, arrow_right_xy)
        
        formula[0].shift(UP*3,RIGHT*2)
        formula[0].set_color(BLUE)
        formula[1].shift(UP*3,RIGHT*8)
        formula[1].set_color(GREEN)
        formula[6].shift(DOWN*1,LEFT*8)
        formula[6].set_color(BLUE)
        formula[7].next_to(formula[6])
        formula[8].next_to(formula[7])
        formula[8].set_color(GREEN)
        group1=VGroup(formula[6], formula[7], formula[8])
        formula_var=MathTex("Var(X+Y)=Var(X)+Var(Y)")
        formula_var.shift(DOWN*1,RIGHT*2)
        formula_var_text=Text("(Assuming that X and Y are independent!)")
        formula_var_text.shift(DOWN*2,RIGHT*2)
        formula_var_text.scale(0.5)
        
        
        self.add(chart_x)
        self.add(formula[0])
        self.add(chart_y)
        self.add(formula[1])
        self.add(mean_line_std_left_x,mean_line_std_right_x,
                 mean_line_std_left_y,mean_line_std_right_y,
                 mean_line_x,mean_line_y)
        self.add(arrow_left_x, arrow_right_x, arrow_left_y, arrow_right_y)
        
        group2=VGroup(mean_line_std_left_x,mean_line_std_right_x,
                 mean_line_std_left_y,mean_line_std_right_y,
                 mean_line_x,mean_line_y)
        group3=VGroup(mean_line_std_left_xy,mean_line_std_right_xy,mean_line_xy)
        self.play(ReplacementTransform(chart_x.copy(),chart_xy),
                  ReplacementTransform(chart_y.copy(),chart_xy), 
                  ReplacementTransform(group2.copy(),group3),
                  ReplacementTransform(group_arrow.copy(),group_arrow_xy),
                  ReplacementTransform(formula[0].copy(),formula[6]),
                  ReplacementTransform(formula[1].copy(),formula[8]),
                  Create(formula[7]),
                  runtime=2, smooth=True)
        self.play(ReplacementTransform(group1.copy(),formula_var))
        self.play(Write(formula_var_text))
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
   
    def create_bar_chart_y(self, probability_data):
        

        chart = BarChart(
                values=probability_data,
                bar_names=self.value_y,
                bar_colors=[ interpolate_color('#32CD32','#ADFF2F' , x/len(self.value_y)) for x in range(len(self.value_y))],
                y_range=[0, 0.3,0.1],
                x_length=10,
                y_length=5,
                bar_width=1,
                bar_fill_opacity=1,
                bar_stroke_width=0,
            )
        
        return chart
    
    def create_bar_chart_xy(self, probability_data):
        

        chart = BarChart(
                values=probability_data,
                bar_names=self.value_xy,
                y_range=[0, 0.3,0.1],
                bar_colors=[ interpolate_color(LIGHT_BROWN,'#ADFF2F' , x/len(self.value_xy)) for x in range(len(self.value_xy))],
                x_length=15,
                y_length=5,
                bar_width=1,
                bar_fill_opacity=1,
                bar_stroke_width=0,
            )
        
        return chart
    
    
    def calculate_sum_probability_distribution(self,X_values, P_X, Y_values, P_Y):
        # Khởi tạo dict để lưu trữ phân phối xác suất của X + Y
        distribution = {}

        # Tính toán phân phối xác suất
        for x in X_values:
            for y in Y_values:
                sum_value = x + y
                probability = P_X[X_values.index(x)] * P_Y[Y_values.index(y)]

                if sum_value in distribution:
                    distribution[sum_value] += probability
                else:
                    distribution[sum_value] = probability

        return distribution


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
        arrow_left.shift(UP*1)
        arrow_right = Arrow(start=start, end=end_right, color=arrow_color)
        arrow_right.shift(UP*1)
         
        
        return arrow_left, arrow_right