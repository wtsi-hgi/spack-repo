# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbglasso(RPackage):
	"""Adaptive Bayesian Graphical Lasso

	Implements a Bayesian adaptive graphical lasso data-augmented block Gibbs sampler. The sampler simulates the posterior distribution of precision matrices of a Gaussian Graphical Model. This sampler was adapted from the original MATLAB routine proposed in Wang (2012) <doi:10.1214/12-BA729>.
	"""
	
	cran = "abglasso" 

	version("0.1.1", md5="18bd0759cd005c5ac6fb515799b3f3d8")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
