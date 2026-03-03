# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvglasso(RPackage):
	"""Lasso Penalized Precision Matrix Estimation

	Estimates a lasso penalized precision matrix via the blockwise coordinate descent (BCD). This package is a simple wrapper around the popular 'glasso' package that extends and enhances its capabilities. These enhancements include built-in cross validation and visualizations.
              See Friedman et al (2008) <doi:10.1093/biostatistics/kxm045> for details regarding the estimation method.
	"""
	
	homepage = "https://github.com/MGallow/CVglasso"
	cran = "CVglasso" 

	version("1.0", md5="3c9b819c1cf17a25bb62b2cab1ebc622")

	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
