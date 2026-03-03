# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatrixnormal(RPackage):
	"""The Matrix Normal Distribution

	Computes densities, probabilities, and random deviates of the Matrix Normal (Pocuca et al. (2019) <doi:10.48550/arXiv.1910.02859>). Also includes simple but useful matrix functions. See the vignette for more information. 
	"""
	
	cran = "matrixNormal" 

	version("0.1.1", md5="79bb7ca65059b4b1077fbd4158b6eb88")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm@1.1.2:", type=("build", "run"))
