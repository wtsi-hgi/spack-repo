# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastcox(RPackage):
	"""Lasso and Elastic-Net Penalized Cox's Regression in High
Dimensions Models using the Cocktail Algorithm

	We implement a cocktail algorithm, a good mixture of coordinate decent, the majorization-minimization principle and the strong rule, for computing the solution paths of the elastic net penalized Cox's proportional hazards model. The package is an implementation of Yang, Y. and Zou, H. (2013) DOI: <doi:10.4310/SII.2013.v6.n2.a1>.
	"""
	
	homepage = "https://github.com/emeryyi/fastcox"
	cran = "fastcox" 

	version("1.1.3", md5="733d86fd9834b5af2eefee1fee3404d5")

	depends_on("r-matrix", type=("build", "run"))
