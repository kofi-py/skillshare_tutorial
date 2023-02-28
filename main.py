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

        axes = Axes((-1, 6), (-1, 3)).shift(DOWN*1.5)
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        graph = axes.plot(lambda x: 1 / x, x_range=[0.333, 6], color=ORANGE)
        graphing = VGroup(axes, graph, axes_labels)
        self.play(DrawBorderThenFill(axes), Write(axes_labels))
        self.play(Create(graph))
