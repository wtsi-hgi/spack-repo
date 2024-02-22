# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmoip(RPackage):
	"""Tools for 2D and 3D Plots of Single and Multi-Objective
Linear/Integer Programming Models

	Make 2D and 3D plots of linear programming (LP), 
    integer linear programming (ILP), or mixed integer linear programming (MILP) models 
    with up to three objectives. Plots of both the solution and criterion space are possible.
    For instance the non-dominated (Pareto) set for bi-objective LP/ILP/MILP programming models 
    (see vignettes for an overview). The package also contains an function for checking if a point
    is inside the convex hull.
	"""
	
	homepage = "https://relund.github.io/gMOIP/"
	cran = "gMOIP" 

	version("1.5.2", md5="14b3d05e5852b96ff1aeee9413e91fd3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-eaf", type=("build", "run"))
