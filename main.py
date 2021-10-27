from EgalitarianDivision import EgalitarianDivision

mat = [[81, 19, 1],
       [70, 1, 29],
       [98, 1, 1]]

# For this matrix the algorithm will do the following:

# Create variables:
# min_util
# Variables = (x_1, y_1, z_1, x_2, y_2, z_2, x_3, y_3, z_3)
# total of #players∙#resources
# x_i, y_i, z_i is the share of player i for resources 1, 2 and 3 respectively.

# Save in a list the following constraints:

# 1. A player cannot take a negative amount of a resource, therefore
# ∀i: x_i>=0, y_i>=0, z_i>=0

# 2. Each player's V_i(X_i) >= min_util
# For example: for player 1 81*x_1 + 19*y_1 + 1*z_1 >= min_util

# 3. We can take only a sum of 1 from each resource
# For example: for resource 1 x_1 + x_2 + x_3 == 1

# Finds the maximum of min_util given the constraints above.


prob = EgalitarianDivision(mat)
prob.run()
