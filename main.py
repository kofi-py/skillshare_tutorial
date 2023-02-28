from manim import *
import numpy as np


class Example1(Scene):
    def construct(self):
        t1 = Tex("Here is a way to view Euler's number:", color=GOLD_B).to_corner(UP)
        self.play(Write(t1))
        t2 = Tex("Consider the graph of the function", color=BLUE).shift(UP*2.5)
        t2.to_corner(LEFT)
        self.play(Write(t2))
        t3 = MathTex(r"f : \mathbb{R}_+ \to \mathbb{R}, \ f(x) = \frac{1}{x}", color=RED_B).next_to(t2, RIGHT)
        self.play(Write(t3))

        axes = Axes((-1, 6), (-1, 3))
        self.play(Write(axes))