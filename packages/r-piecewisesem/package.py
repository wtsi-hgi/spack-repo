# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPiecewisesem(RPackage):
	"""Piecewise Structural Equation Modeling

	Implements piecewise structural equation modeling from a single
    list of structural equations, with new methods for non-linear, latent, and
    composite variables, standardized coefficients, query-based prediction and
    indirect effects. See <http://jslefche.github.io/piecewiseSEM/> for more.
	"""
	
	homepage = "https://github.com/jslefche/"
	cran = "piecewiseSEM" 

	version("2.3.0", md5="833e952fbad48a0001f0bc9e0468dbb7")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-mumin", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-performance", type=("build", "run"))
