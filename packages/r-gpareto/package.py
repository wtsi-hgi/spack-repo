# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpareto(RPackage):
	"""Gaussian Processes for Pareto Front Estimation and Optimization

	Gaussian process regression models, a.k.a. Kriging models, are
    applied to global multi-objective optimization of black-box functions.
    Multi-objective Expected Improvement and Step-wise Uncertainty Reduction
    sequential infill criteria are available. A quantification of uncertainty
    on Pareto fronts is provided using conditional simulations.
	"""
	
	homepage = "https://github.com/mbinois/GPareto"
	cran = "GPareto" 

	version("1.1.8", md5="c34463696a8c801ddd1a9b31d28df3b8")

	depends_on("r-dicekriging", type=("build", "run"))
	depends_on("r-emoa", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rgenoud", type=("build", "run"))
	depends_on("r-pbivnorm", type=("build", "run"))
	depends_on("r-pso", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-kriginv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-dicedesign", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
