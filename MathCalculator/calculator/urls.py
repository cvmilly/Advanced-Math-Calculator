from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('algebra/', views.algebra, name="algebra"),
    path('algebra/equations', views.algebra_equations, name="algebra_equations"),
    path('algebra/equations/solve-equation', views.algebra_equations_solve_equation, name="algebra_equations_solve_equation"),
    path('algebra/equations/system', views.algebra_equations_system, name="algebra_equations_system"),
    path('algebra/equations/evaluate-expression', views.algebra_equations_expressions, name="algebra_equations_expressions"),
    path('algebra/slope', views.algebra_slope, name="algebra_slope"),
    path('algebra/graph', views.algebra_graph, name="algebra_graph"),
    path('algebra/function-composition', views.algebra_composition, name="algebra_composition"),
    path('algebra/partial-fractions', views.algebra_partial_fractions, name="algebra_partial_fractions"),
    path('calculus', views.calculus, name="calculus"),
    path('calculus/derivatives', views.calculus_derivatives, name="calculus_derivatives"),
    path('calculus/derivatives/standard', views.calculus_derivatives_standard, name="calculus_derivatives_standard"),
    path('calculus/derivatives/partial', views.calculus_derivatives_partial, name="calculus_derivatives_partial"),
    path('calculus/integrals', views.calculus_integrals, name="calculus_integrals"),
    path('calculus/integrals/indefinite', views.calculus_integrals_indefinite, name="calculus_integrals_indefinite"),
    path('calculus/integrals/definite', views.calculus_integrals_definite, name="calculus_integrals_definite"),
    path('calculus/graphical', views.calculus_graphical, name="calculus_graphical"),
    path('calculus/graphical/arc-length', views.calculus_graphical_arc_length, name="calculus_graphical_arc_length"), # new
    path('calculus/graphical/tangent-line', views.calculus_graphical_tangent_line, name="calculus_graphical_tangent_line"), # new
    path('calculus/graphical/critical-points', views.calculus_graphical_critical_points, name="calculus_graphical_critical_points"), # new
    path('calculus/limits', views.calculus_limits, name="calculus_limits"),
    path('ordinary-differential-equation', views.ODE, name="ODE"), # new
    path('ordinary-differential-equation/first-order', views.ODE_first, name="ODE_first"), # new
    path('ordinary-differential-equation/first-order/linear', views.ODE_first_linear, name="ODE_first_linear"), # new
    path('ordinary-differential-equation/first-order/separable', views.ODE_first_separable, name="ODE_first_separable"), # new
    path('ordinary-differential-equation/first-order/exact', views.ODE_first_exact, name="ODE_first_exact"), # new
    path('ordinary-differential-equation/first-order/euler', views.ODE_first_euler, name="ODE_first_euler"), # new
    path('ordinary-differential-equation/second-order', views.ODE_second, name="ODE_second"), # new
    path('ordinary-differential-equation/second-order/homgenous', views.ODE_second_homogenous, name="ODE_second_homogenous"), # new
    path('linear-algebra', views.linear_algebra, name="linear_algebra"), # new
    path('linear-algebra/matrix-on-matrix', views.linear_algebra_matrix_ops, name="linear_algebra_matrix_ops"), # new
    path('linear-algebra/matrix-on-matrix/multiplication', views.linear_algebra_matrix_ops_multiplication, name="linear_algebra_matrix_ops_multiplication"), # new
    path('linear-algebra/matrix-on-matrix/addition', views.linear_algebra_matrix_ops_addition, name="linear_algebra_matrix_ops_addition"), # new
    path('linear-algebra/matrix-on-matrix/matrix-equation', views.linear_algebra_matrix_ops_equation, name="linear_algebra_matrix_ops_equation"), # new
    path('linear-algebra/system', views.linear_algebra_system, name="linear_algebra_system"), # new
    path('linear-algebra/matrix-info', views.linear_algebra_info, name="linear_algebra_info"), # new
    path('linear-algebra/matrix-info/reduced-row-echelon-form', views.linear_algebra_info_RREF, name="linear_algebra_info_RREF"), # new
    path('linear-algebra/matrix-info/determinant', views.linear_algebra_info_determinant, name="linear_algebra_info_determinant"), # new
    path('linear-algebra/matrix-info/transpose', views.linear_algebra_info_transpose, name="linear_algebra_info_transpose"), # new
    path('linear-algebra/matrix-info/inverse', views.linear_algebra_info_inverse, name="linear_algebra_info_inverse"), # new
    path('linear-algebra/matrix-info/linear-independence', views.linear_algebra_info_LI, name="linear_algebra_info_LI"), # new
    path('geometry', views.geometry, name="geometry") # new
]
