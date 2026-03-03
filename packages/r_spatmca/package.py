# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatmca(RPackage):
	"""Regularized Spatial Maximum Covariance Analysis

	Provide regularized maximum covariance analysis incorporating smoothness,
  sparseness and orthogonality of couple patterns by using the alternating direction method
  of multipliers algorithm. The method can be applied to either regularly or irregularly
  spaced data,  including 1D, 2D, and 3D (Wang and Huang, 2017 <doi:10.1002/env.2481>).
	"""
	
	homepage = "https://github.com/egpivo/SpatMCA"
	cran = "SpatMCA" 

	version("1.0.4", md5="6575236a324bc25049c0a40a6ee32750")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
