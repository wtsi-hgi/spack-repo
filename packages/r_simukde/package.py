# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimukde(RPackage):
	"""Simulation with Kernel Density Estimation

	Generates random values from a univariate and multivariate continuous distribution by using kernel density estimation based on a sample. Duong (2017) <doi:10.18637/jss.v021.i07>, Christian P. Robert and George Casella (2010 ISBN:978-1-4419-1575-7) <doi:10.1007/978-1-4419-1576-4>.
	"""
	
	homepage = "https://github.com/galaamn/simukde"
	cran = "simukde" 

	version("1.3.0", md5="5db462e5c5d2a95fb540da34ada9f55b")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
