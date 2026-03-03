# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPartr2(RPackage):
	"""Partitioning R2 in GLMMs

	Partitioning the R2 of GLMMs into variation explained by each 
    predictor and combination of predictors using semi-partial (part) R2 and
    inclusive R2. Methods are based on the R2 for GLMMs described in
    Nakagawa & Schielzeth (2013) and Nakagawa, Johnson & Schielzeth (2017).
	"""
	
	homepage = "https://github.com/mastoffel/partR2"
	cran = "partR2" 

	version("0.9.2", md5="de77b3140cce5062a4ca3ec6f24887a3", url="https://cran.r-project.org/src/contrib/partR2_0.9.2.tar.gz")
	version("0.9.1", md5="4e335f212722e043f8319997986a3b52", url="https://cran.r-project.org/src/contrib/partR2_0.9.1.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lme4@1.1.21:", type=("build", "run"))
	depends_on("r-pbapply@1.4.2:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-rlang@0.4.2:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
