from Circle import Circle
from Point import Point
from PlotOptions import PlotOptions
import matplotlib.pyplot as plt
import numpy as np


def generate_equidistant_points_on_circle(number_of_points, center_of_circle, radius_of_circle, start_angle = 0):
    # On va générer les pts de tracés en hackant le tracé du cercle
    # number_of_points + 1 to get the right number of points in the linespace
    CirclePoints = Circle(PlotOptions(number_of_points + 1, 1, radius_of_circle), center_of_circle, radius_of_circle).drawSemiCircle(start_angle, 2 * np.pi)
    return [Point(CirclePoints[0][i], CirclePoints[1][i]) for i in range(len(CirclePoints[0]))]

def drawCircles(circles_list, fig):
    for c in circles_list :
        xy_plot = c.drawCircle()
        fig.plot(xy_plot[0], xy_plot[1], color="black")

def drawSimpleRosette(Center = Point(), r = 1, start_angle = 0, nb_points_resolution = 10000, dpi = 300):
    plot_opt = PlotOptions(nb_points_resolution, dpi, r)
    circL = [Circle(plot_opt, x, r) for x in generate_equidistant_points_on_circle(6, Center, r, start_angle)]
    circL.append(Circle(plot_opt, Center, r))

    fig, a1 = plt.subplots(1)
    a1.set_aspect(1)
    drawCircles(circL, a1)
    plt.show()

def drawDoubleRosette(Center=Point(), r=1, start_angle=0, nb_points_resolution=10000, dpi=300):
    plot_opt = PlotOptions(nb_points_resolution, dpi, r)
    circL = [Circle(plot_opt, x, r) for x in generate_equidistant_points_on_circle(12, Center, r, start_angle)]
    circL.append(Circle(plot_opt, Center, r))

    fig, a1 = plt.subplots(1)
    a1.set_aspect(1)
    drawCircles(circL, a1)
    plt.show()

if __name__ == "__main__":
    print("Unit test draw rosettes :")
    print("\tDraw Double Rosette :")
    drawDoubleRosette()
    print("\tDraw Simple Rosette with angle:")
    drawSimpleRosette(Point(), 1, np.pi / 2)
