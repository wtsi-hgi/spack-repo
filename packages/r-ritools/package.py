# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRitools(RPackage):
	"""Randomization Inference Tools

	Tools for randomization-based inference. Current focus is on the d^2 omnibus test of differences of means following Hansen and Bowers (2008)  <doi:10.1214/08-STS254> . This test is useful for assessing balance in matched observational studies or for analysis of outcomes in block-randomized experiments.
	"""
	
	homepage = "https://cran.r-project.org/package=RItools"
	cran = "RItools" 

	version("0.3-3", md5="3798a753e0cb845ed1151f56e1097941")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-svd", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
