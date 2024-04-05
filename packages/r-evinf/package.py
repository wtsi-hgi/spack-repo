# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvinf(RPackage):
	"""Inference with Extreme Value Inflated Count Data

	Allows users to model and draw inferences from extreme value inflated count data, and to evaluate these models and compare to non extreme-value inflated counterparts. The package is built to be compatible with standard presentation tools such as 'broom', 'tidy', and 'modelsummary'.
	"""
	
	homepage = "https://github.com/Doktorandahl/evinf"
	cran = "evinf" 

	version("0.8.8", md5="47d460dc8ad21a5bb8080b8a7f16d3f7")
	version("0.8.7", md5="4b441ab6164d9cf110490136d22413ee")

	depends_on("r-generics", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-mistr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-mlmetrics", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
