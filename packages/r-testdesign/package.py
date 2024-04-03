# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTestdesign(RPackage):
	"""Optimal Test Design Approach to Fixed and Adaptive Test
Construction

	Uses the optimal test design approach by Birnbaum (1968, ISBN:9781593119348) and
    van der Linden (2018) <doi:10.1201/9781315117430> to construct fixed, adaptive, and parallel tests.
    Supports the following mixed-integer programming (MIP) solver packages: 'Rsymphony',
    'gurobi', 'lpSolve', and 'Rglpk'. The 'gurobi' package is not available from CRAN; see <https://www.gurobi.com/downloads/>.
	"""
	
	homepage = "https://choi-phd.github.io/TestDesign/"
	cran = "TestDesign" 

	version("1.6.1", md5="9086977897629c26fa7e1f58ad5c097e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-logitnorm", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
