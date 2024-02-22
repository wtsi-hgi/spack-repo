# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKaren(RPackage):
	"""Kalman Reaction Networks

	This is a stochastic framework that combines biochemical reaction networks with extended Kalman filter and Rauch-Tung-Striebel smoothing. 
  This framework allows to investigate the dynamics of cell differentiation from high-dimensional clonal tracking data subject to measurement noise, false negative errors, and systematically unobserved cell types. 
  Our tool can provide statistical support to biologists in gene therapy clonal tracking studies for a deeper understanding of clonal reconstitution dynamics. Further details on the methods can be found in L. Del Core et al., (2022) <doi:10.1101/2022.07.08.499353>.
	"""
	
	cran = "Karen" 

	version("1.0", md5="51ae9e904621b66f92b9f08e01e97a1d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-gaussquad", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
