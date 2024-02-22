# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultibd(RPackage):
	"""Multivariate Birth-Death Processes

	Computationally efficient functions to provide direct likelihood-based
    inference for partially-observed multivariate birth-death processes.  Such processes
    range from a simple Yule model to the complex susceptible-infectious-removed model
    in disease dynamics.  Efficient likelihood evaluation facilitates maximum likelihood
    estimation and Bayesian inference.
	"""
	
	cran = "MultiBD" 

	version("0.2.0", md5="f1aa1502408ce88e5e2cd0431c389b02")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
