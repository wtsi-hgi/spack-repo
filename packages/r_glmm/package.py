# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmm(RPackage):
	"""Generalized Linear Mixed Models via Monte Carlo Likelihood
Approximation

	Approximates the likelihood of a generalized linear mixed model using Monte Carlo likelihood approximation. Then maximizes the likelihood approximation to return maximum likelihood estimates, observed Fisher information, and other model information.
	"""
	
	cran = "glmm" 

	version("1.4.4", md5="3d837cccb3a856ebf573c44c63b46379")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-trust", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-itertools", type=("build", "run"))
