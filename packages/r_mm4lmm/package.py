# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMm4lmm(RPackage):
	"""Inference of Linear Mixed Models Through MM Algorithm

	The main function MMEst() performs (Restricted) Maximum Likelihood in a variance component mixed models using a Min-Max (MM) algorithm (Laporte, F., Charcosset, A. & Mary-Huard, T. (2022) <doi:10.1371/journal.pcbi.1009659>).
	"""
	
	cran = "MM4LMM" 

	version("3.0.2", md5="9bce50091e342b1d56fd757266e3e8bf")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
