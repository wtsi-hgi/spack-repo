# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRar(RPackage):
	"""Risk-Adjusted Regression

	Perform risk-adjusted regression and sensitivity analysis as
    developed in "Mitigating Omitted- and Included-Variable Bias in Estimates of
    Disparate Impact" Jung et al. (2024) <arXiv:1809.05651>.
	"""
	
	homepage = "https://rar.jgaeb.com"
	cran = "rar" 

	version("0.0.3", md5="c27b8af9e5c8188592eaa2049b7f6ca2")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
