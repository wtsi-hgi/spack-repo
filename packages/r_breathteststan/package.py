# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreathteststan(RPackage):
	"""Stan-Based Fit to Gastric Emptying Curves

	Stan-based curve-fitting function
  for use with package 'breathtestcore' by the same author.
  Stan functions are refactored here for easier testing.
	"""
	
	homepage = "https://github.com/dmenne/breathteststan"
	cran = "breathteststan" 

	version("0.8.5", md5="09ff4106c4deba7e95768403bc8193b8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-breathtestcore@0.8.4:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
	depends_on("r-bh@1.72:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
