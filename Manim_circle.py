from manim import *

class manim_Crcl(Scene):
    def construct(self):
        C1 = Circle(radius=2,fill_color=BLUE,fill_opacity=0.5,stroke_color=YELLOW_A)
        Txt1=Text("Circle using Manim").next_to(C1,UP)
        #self.add(C1,Txt1)
        self.play(Create(C1),Create(Txt1),run_time=2)




