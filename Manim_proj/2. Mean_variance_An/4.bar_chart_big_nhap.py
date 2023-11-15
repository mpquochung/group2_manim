from manim import *
class Bar_chart_x17_nhap(MovingCameraScene):
    def construct(self):
        prob = {    1:0.4,
                    2:0.25,
                    3:0.15,
                    4:0.1,
                    5:0.07,
                    6:0.03}
        charts=[]
        chart_names = ["X1", "X1+X2", "X1+X2+X3", "X1+X2+X3+X4", "X1+X2+X3+X4+X5", "X1+X2+X3+X4+X5+X6", "X1+X2+X3+X4+X5+X6+X7"]
        
        prob_x=[0.4,0.25,0.15,0.1,0.07,0.03]
        x_value=[1,2,3,4,5,6]
        for n in range(1, 8):  # Tạo 8 biểu đồ với n từ 1 đến 8 (X1,X1+X2,...,X1+X2+...+X7)
            self.n=n
            result_dict = self.dice_sum(prob, self.n)
            self.keys = list(result_dict.keys())
            values = list(result_dict.values())
            mean_value=self.calculate_mean(values)
            
            chart = self.create_bar_chart(values)
            mean_line_x=self.mean_line(chart, mean_value)
            
            group_chart = VGroup(chart, mean_line_x)
            charts.append(group_chart)
        
        
        charts[0].shift(UP*3,LEFT*4.8)
        charts[0].scale(0.3)
        charts[1].shift(UP*1.8,LEFT*4)
        charts[1].scale(0.3)
        charts[2].shift(UP*0.5,LEFT*4)
        charts[2].scale(0.3)
        charts[3].shift(DOWN*0.8,LEFT*4)
        charts[3].scale(0.3)
        charts[4].shift(DOWN*2,LEFT*4)
        charts[4].scale(0.3)
        charts[5].shift(DOWN*3,LEFT*4)
        charts[5].scale(0.3)
        charts[6].shift(DOWN*4,LEFT*4)
        charts[6].scale(0.3)

        chart_name_0=Text(chart_names[0]).next_to(charts[0], RIGHT).scale(0.5)
        chart_name_1=Text(chart_names[1]).next_to(charts[1], RIGHT).scale(0.5)
        chart_name_2=Text(chart_names[2]).next_to(charts[2], RIGHT).scale(0.5)
        chart_name_3=Text(chart_names[3]).next_to(charts[3], RIGHT).scale(0.5)
        chart_name_4=Text(chart_names[4]).next_to(charts[4], RIGHT).scale(0.5)
        chart_name_5=Text(chart_names[5]).next_to(charts[5], RIGHT).scale(0.5)
        chart_name_6=Text(chart_names[6]).next_to(charts[6], RIGHT).scale(0.5)
        group0=VGroup(chart_name_0,charts[0])
        group1=VGroup(chart_name_1,charts[1])
        group2=VGroup(chart_name_2,charts[2])
        group3=VGroup(chart_name_3,charts[3])
        group4=VGroup(chart_name_4,charts[4])
        group5=VGroup(chart_name_5,charts[5])
        group6=VGroup(chart_name_6,charts[6])
        self.add(group0,group1,group2,group3,group4,group5,group6)
        self.wait(3)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.scale(0.5).move_to(charts[0]))
        self.wait(0.2)
        self.play(self.camera.frame.animate.move_to(charts[1]))
        self.wait(0.2)
        self.play(self.camera.frame.animate.move_to(charts[2]))
        self.wait(0.2)
        self.play(self.camera.frame.animate.move_to(charts[3]))
        self.wait(0.2)
        self.play(self.camera.frame.animate.move_to(charts[4]))
        self.wait(0.2)
        self.play(self.camera.frame.animate.move_to(charts[5]))
        self.wait(0.2)
        self.play(self.camera.frame.animate.move_to(charts[6]))
        self.play(Restore(self.camera.frame))
        self.wait(3)

    def create_bar_chart(self, probability_data):
        if self.n==1:
            y_range = [0, 0.5, 0.1]
        else:
            y_range = [0, 0.2, 0.1]
        chart = BarChart(
                values=probability_data,
                bar_names=self.keys,
                
                y_range=y_range,
                
                y_length=2,
                bar_width=1,
                bar_fill_opacity=1,
                bar_stroke_width=0,
            )
        
        return chart
    
    
    def calculate_mean(self, probability_data):
        mean_data = sum((i + 1) * p for i, p in enumerate(probability_data))
        return mean_data
    
    
    def mean_line(self, chart, mean_data):
        max_prob = max(chart.values)
        mean_line = Line(
            start=chart.get_x_axis().n2p(mean_data),
            end=[chart.get_x_axis().n2p(mean_data)[0], chart.get_y_axis().n2p(max_prob*1.2)[1], 0],
            color=PINK,stroke_opacity=0.5
        )
        mu_text = r"\mu" if self.n == 1 else f"{self.n}\mu "
        
        mu = MathTex(mu_text + "=" + str(round(mean_data, 2))).next_to(mean_line, UP).set_color(PINK)
        return VGroup(mean_line, mu)
    
    
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
            