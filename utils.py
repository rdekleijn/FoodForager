import math

import numpy as np


def calc_new_location(position, orientation, speed):
    orientation *= math.pi / 180
    new_x = position[0] + (speed * math.cos(orientation))
    new_y = position[1] + (speed * math.sin(orientation))
    return [new_x, new_y]


def update_position(agent):
    """Takes a current state, an action vector, and returns the new state"""

    orientation = agent.orientation * math.pi / 180
    new_x = agent.position[0] + (agent.motor_output[0] * math.cos(orientation))
    new_y = agent.position[1] + (agent.motor_output[0] * math.sin(orientation))
    new_orientation = agent.orientation + agent.motor_output[1]
    agent.position[0] = new_x
    agent.position[1] = new_y
    agent.orientation = new_orientation
    return agent


def calc_distance(x1, y1, size1, x2, y2, size2):
    return (np.sqrt(np.square(x1-x2) + np.square(y1-y2))) - size1/2 - size2/2


# def circle_line_collision(p1, p2, circle_center, radius):
# #     Input
# #     LineP1
# #     Point
# #     First
# #     point
# #     describing
# #     the
# #     line
# #     LineP2
# #     Point
# #     Second
# #     point
# #     describing
# #     the
# #     line
# #     CircleCentre
# #     Point
# #     The
# #     centre
# #     of
# #     the
# #     circle
# #     Radius
# #     Floating - point
# #     The
# #     circle
# #     's radius
# #
# #
# # Output
# # The
# # point(s)
# # of
# # the
# # collision, or null if no
# # collision
# # exists.
#
# # Transform to local coordinates
#     LocalP1 = p1 - circle_center
#     LocalP2 = p2 - circle_center
#     # Precalculate this value. We use it often
#     P2MinusP1 = LocalP2 - LocalP1
#
#     a = (P2MinusP1.X) * (P2MinusP1.X) + (P2MinusP1.Y) * (P2MinusP1.Y)
#     b = 2 * ((P2MinusP1.X * LocalP1.X) + (P2MinusP1.Y * LocalP1.Y))
#     c = (LocalP1.X * LocalP1.X) + (LocalP1.Y * LocalP1.Y) – (Radius * Radius)
#     delta = b * b – (4 * a * c)
#     if (delta < 0) // No intersection
#         return null;
#     else if (delta == 0) // One intersection
#         u = -b / (2 * a)
#         return LineP1 + (u * P2MinusP1)
#         /* Use LineP1 instead of LocalP1 because we want our answer in global
#            space, not the circle's local space */
#     else if (delta > 0) // Two intersections
#         SquareRootDelta = sqrt(delta)
#
#         u1 = (-b + SquareRootDelta) / (2 * a)
#         u2 = (-b - SquareRootDelta) / (2 * a)
#
#         return { LineP1 + (u1 * P2MinusP1) ; LineP1 + (u2 * P2MinusP1)}
