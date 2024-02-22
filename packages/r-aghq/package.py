# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAghq(RPackage):
	"""Adaptive Gauss Hermite Quadrature for Bayesian Inference

	Adaptive Gauss Hermite Quadrature for Bayesian inference.
    The AGHQ method for normalizing posterior distributions
    and making Bayesian inferences based on them. Functions are provided for doing
    quadrature and marginal Laplace approximations, and summary methods are provided
    for making inferences based on the results. 
    See Stringer (2021). "Implementing Adaptive Quadrature for Bayesian Inference: 
    the aghq Package" <arXiv:2101.04468>.
	"""
	
	cran = "aghq" 

	version("0.4.1", md5="2f55ef4432eb344824ee34b01ef3a7c5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvquad", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
