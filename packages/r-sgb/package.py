# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgb(RPackage):
	"""Simplicial Generalized Beta Regression

	Main properties and regression procedures using a generalization of the Dirichlet distribution called Simplicial Generalized Beta distribution. It is a new distribution on the simplex (i.e. on the space of compositions or positive vectors with sum of components equal to 1). The Dirichlet distribution can be constructed from a random vector of independent Gamma variables divided by their sum. The SGB follows the same construction with generalized Gamma instead of Gamma variables. The Dirichlet exponents are supplemented by an overall shape parameter and a vector of scales. The scale vector is itself a composition and can be modeled with auxiliary variables through a log-ratio transformation. Graf, M. (2017, ISBN: 978-84-947240-0-8). See also the vignette enclosed in the package.
	"""
	
	cran = "SGB" 

	version("1.0.1.1", md5="10d3b325d5eebbad2df9c75e77eeeef8")

	depends_on("r-formula", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
