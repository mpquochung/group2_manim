from manim import *


class cthuc(Scene):
    def construct(self):
        
        mean_ct_text=MathTex(r"Mean: \mu = E(X)=  \sum_{x}P(X=x) . x").set_color(PINK)
        var_ct_text=MathTex(r'''Variance: Var(X)= \sigma^2 =  E[(X- \mu)^2] \\= 
                       E[(X-E[X])^2] \\= E[X^2 - 2XE[X] + E[X]^2] \\= 
                       E[X^2] - 2E[X]E[X]+E[X]^2 \\=E[X^2] - E[X]^2''').set_color(YELLOW)
        var_ct_text.shift(DOWN)
        std_ct_text=MathTex(r"Standard \hspace{0.15cm} deviation:\\ \sigma = \sqrt{Var(X)}").set_color(BLUE)
        std_ct_text.shift(RIGHT*3,DOWN*1)
        
        mean_ct_text.generate_target()
        var_ct_text.generate_target()
        std_ct_text.generate_target()
        
        self.play(Write(mean_ct_text))
        
        mean_ct_text.target.shift(UP*2)
        self.play(MoveToTarget(mean_ct_text))
        self.play(Write(var_ct_text))
        self.wait(3)
        var_ct_text.target.shift(LEFT*3)
        var_ct_text.target.scale(0.6)
        self.play(MoveToTarget(var_ct_text))
        self.play(ReplacementTransform(var_ct_text.copy(),std_ct_text))
        self.wait(2)