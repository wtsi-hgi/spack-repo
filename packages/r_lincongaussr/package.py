# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLincongaussr(RPackage):
	"""Sampling Multivariate Normal Distribution under Linear
Constraints

	Sample truncated multivariate Normal distribution following Gessner, A., Kanjilal, O., & Hennig, P. (2019). Integrals over Gaussians under Linear Domain Constraints. 108. <arxiv:1910.09328>.
	"""
	
	homepage = "https://github.com/YunyiShen/linconGaussR"
	cran = "linconGaussR" 

	version("0.1", md5="5ff6477ed0527b6f85c0b1932f7e9b75")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
