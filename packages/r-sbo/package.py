# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbo(RPackage):
	"""Text Prediction via Stupid Back-Off N-Gram Models

	Utilities for training and evaluating text predictors based on Stupid Back-Off N-gram models (Brants et al., 2007, <https://www.aclweb.org/anthology/D07-1090/>).
	"""
	
	homepage = "https://vgherard.github.io/sbo/"
	cran = "sbo" 

	version("0.5.0", md5="b49731ee7ca8c65c47643063c5933afb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
