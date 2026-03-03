# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGglm(RPackage):
	"""Grammar of Graphics for Linear Model Diagnostic Plots

	Allows for easy creation of diagnostic plots for a variety of model objects using the Grammar of Graphics.  
  Provides functionality for both individual diagnostic plots and an array of four standard diagnostic plots.
	"""
	
	homepage = "https://github.com/graysonwhite/gglm"
	cran = "gglm" 

	version("1.0.3", md5="e9fc35739f3518ec0af22af1f41702dd")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-broom-mixed", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
