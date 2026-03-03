# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNaive(RPackage):
	"""Empirical Extrapolation of Time Feature Patterns

	An application for the empirical extrapolation of time features selecting and summarizing the most relevant patterns in time sequences.
	"""
	
	homepage = "https://rpubs.com/giancarlo_vercellino/naive"
	cran = "naive" 

	version("1.2.3", md5="ab951c2a40617b06a033bf2070a47194")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-purrr@1.0.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.2:", type=("build", "run"))
	depends_on("r-readr@2.1.4:", type=("build", "run"))
	depends_on("r-lubridate@1.9.2:", type=("build", "run"))
	depends_on("r-imputets@3.3:", type=("build", "run"))
	depends_on("r-fancova@0.6.1:", type=("build", "run"))
	depends_on("r-scales@1.2.1:", type=("build", "run"))
	depends_on("r-tictoc@1.2:", type=("build", "run"))
	depends_on("r-modeest@2.4:", type=("build", "run"))
	depends_on("r-moments@0.14.1:", type=("build", "run"))
	depends_on("r-greybox@1.0.8:", type=("build", "run"))
	depends_on("r-rfast@2.0.7:", type=("build", "run"))
	depends_on("r-fastdummies@1.6.3:", type=("build", "run"))
	depends_on("r-entropy@1.3.1:", type=("build", "run"))
	depends_on("r-philentropy@0.7:", type=("build", "run"))
