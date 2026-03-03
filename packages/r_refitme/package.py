# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRefitme(RPackage):
	"""Measurement Error Modelling using MCEM

	Fits measurement error models using Monte Carlo Expectation Maximization (MCEM). For specific details on the methodology, see: Greg C. G. Wei & Martin A. Tanner (1990) A Monte Carlo Implementation of the EM Algorithm and the Poor Man's Data Augmentation Algorithms, Journal of the American Statistical Association, 85:411, 699-704 <doi:10.1080/01621459.1990.10474930> For more examples on measurement error modelling using MCEM, see the 'RMarkdown' vignette: "'refitME' R-package tutorial".
	"""
	
	cran = "refitME" 

	version("1.2.2", md5="461a618de9052963cf8d48f83b661d99")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-semipar", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-vgamdata", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
