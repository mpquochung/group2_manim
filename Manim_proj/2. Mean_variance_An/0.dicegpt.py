from manim import *

class DieFace(Mobject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        die = Square(side_length=2, stroke_width=2, fill_color=BLUE, fill_opacity=1)
        die.set(width=2, height=2)
        self.add(die)


class Face1(DieFace):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        dot5 = Dot(radius=0.1, color=WHITE).move_to([0, 0, 0])  # Center
        self.add(dot5)


class Face2(DieFace):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        dot1 = Dot(radius=0.1, color=WHITE).move_to([-0.7, 0.7, 0])  # Top left
        dot3 = Dot(radius=0.1, color=WHITE).move_to([0.7, -0.7, 0])  # Bottom right
        self.add(dot1, dot3)

# ... (other face classes)
class Face3(DieFace):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        dot1 = Dot(radius=0.1, color=WHITE).move_to([-0.7, 0.7, 0])  # Top left
        dot3 = Dot(radius=0.1, color=WHITE).move_to([0.7, -0.7, 0])  # Bottom right
        dot5 = Dot(radius=0.1, color=WHITE).move_to([0, 0, 0])  # Center
        self.add(dot1, dot3, dot5)

class Face4(DieFace):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        dot1 = Dot(radius=0.1, color=WHITE).move_to([-0.7, 0.7, 0])  # Top left
        dot2 = Dot(radius=0.1, color=WHITE).move_to([-0.7, -0.7, 0])  # Bottom left
        dot3 = Dot(radius=0.1, color=WHITE).move_to([0.7, -0.7, 0])  # Bottom right
        dot4 = Dot(radius=0.1, color=WHITE).move_to([0.7, 0.7, 0])  # Top right
        self.add(dot1, dot2, dot3, dot4)
    
class Face5(DieFace):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        dot1 = Dot(radius=0.1, color=WHITE).move_to([-0.7, 0.7, 0])  # Top left
        dot2 = Dot(radius=0.1, color=WHITE).move_to([-0.7, -0.7, 0])  # Bottom left
        dot3 = Dot(radius=0.1, color=WHITE).move_to([0.7, -0.7, 0])  # Bottom right
        dot4 = Dot(radius=0.1, color=WHITE).move_to([0.7, 0.7, 0])  # Top right
        dot5 = Dot(radius=0.1, color=WHITE).move_to([0, 0, 0])  # Center
        self.add(dot1, dot2, dot3, dot4, dot5)

class Face6(DieFace):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        dot1 = Dot(radius=0.1, color=WHITE).move_to([-0.7, 0.7, 0])  # Top left
        dot2 = Dot(radius=0.1, color=WHITE).move_to([-0.7, -0.7, 0])  # Bottom left
        dot3 = Dot(radius=0.1, color=WHITE).move_to([0.7, -0.7, 0])  # Bottom right
        dot4 = Dot(radius=0.1, color=WHITE).move_to([0.7, 0.7, 0])  # Top right
        dot6 = Dot(radius=0.1, color=WHITE).move_to([-0.7, 0, 0])  # Middle left
        dot7 = Dot(radius=0.1, color=WHITE).move_to([0.7, 0, 0])  # Middle right
        self.add(dot1, dot2, dot3, dot4, dot6, dot7)
        
