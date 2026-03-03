# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStratsel(RPackage):
	"""Strategic Selection Estimator

	Provides functions to estimate a strategic selection estimator. A strategic selection estimator is an agent error model in which the two random components are not assumed to be orthogonal. In addition this package provides generic functions to print and plot objects of its class as well as the necessary functions to create tables for LaTeX. There is also a function to create dyadic data sets.
	"""
	
	cran = "StratSel" 

	version("1.3", md5="4dab35ad859f401ae1c9e8e2d3ddb717")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-memisc", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-pbivnorm", type=("build", "run"))
