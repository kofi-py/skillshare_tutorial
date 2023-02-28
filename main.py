from manim import *
import numpy as np


# Section 1 - Basics with Text - 2.28 10:52 AM
class Example1(Scene):
    def construct(self):
        t1 = Tex("Here is a way to view Euler's number:", color=GOLD_B).to_corner(UP)
        self.play(Write(t1))
        
