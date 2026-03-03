# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMagi(RPackage):
	"""MAnifold-Constrained Gaussian Process Inference

	Provides fast and accurate inference for the parameter estimation problem in Ordinary Differential
    Equations, including the case when there are unobserved system components. Implements the MAGI method
    (MAnifold-constrained Gaussian process Inference) of Yang, Wong, and Kou (2021) <doi:10.1073/pnas.2020397118>.
	"""
	
	homepage = "https://arxiv.org/abs/2203.06066"
	cran = "magi" 

	version("1.2.2", md5="a6cab24487801c614d17d9ae9c1569b6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gridbase", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-roptim", type=("build", "run"))
