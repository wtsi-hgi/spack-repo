# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGbp(RPackage):
	"""A Bin Packing Problem Solver

	Basic infrastructure and several algorithms for 1d-4d bin packing
    problem. This package provides a set of c-level classes and solvers for
    1d-4d bin packing problem, and an r-level solver for 4d bin packing problem,
    which is a wrapper over the c-level 4d bin packing problem solver.
    The 4d bin packing problem solver aims to solve bin packing problem, a.k.a
    container loading problem, with an additional constraint on weight.
    Given a set of rectangular-shaped items, and a set of rectangular-shaped bins
    with weight limit, the solver looks for an orthogonal packing solution
    such that minimizes the number of bins and maximize volume utilization.
    Each rectangular-shaped item i = 1, .. , n is characterized by length l_i,
    depth d_i, height h_i, and weight w_i, and each rectangular-shaped bin
    j = 1, .. , m is specified similarly by length l_j, depth d_j, height h_j,
    and weight limit w_j.
    The item can be rotated into any orthogonal direction, and no further
    restrictions implied.
	"""
	
	homepage = "https://github.com/gyang274/gbp"
	cran = "gbp" 

	version("0.1.0.4", md5="b37dfc24a027a66cd53f7d2f289a5900")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
