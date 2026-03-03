# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesianglasso(RPackage):
	"""Bayesian Graphical Lasso

	Implements a data-augmented block Gibbs sampler for simulating the posterior distribution of concentration matrices for specifying the topology and parameterization of a Gaussian Graphical Model (GGM). This sampler was originally proposed in Wang (2012) <doi:10.1214/12-BA729>.
	"""
	
	cran = "BayesianGLasso" 

	version("0.2.0", md5="595557684bf59ac002bc5dcb5e0288a0")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
