# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSensitivity(RPackage):
	"""Global Sensitivity Analysis of Model Outputs and Importance
Measures

	A collection of functions for sensitivity analysis of model outputs (factor screening, global sensitivity analysis and robustness analysis), for variable importance measures of data, as well as for interpretability of machine learning models. Most of the functions have to be applied on scalar output, but several functions support multi-dimensional outputs.
	"""
	
	cran = "sensitivity" 

	version("1.30.0", md5="03c7a6d806fb83ababaa28a0f72f9456")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dtwclust", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
