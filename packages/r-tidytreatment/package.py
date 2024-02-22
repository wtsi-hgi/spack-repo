# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidytreatment(RPackage):
	"""Tidy Methods for Bayesian Treatment Effect Models

	Functions for extracting tidy data from Bayesian treatment effect models, in particular BART, but extensions are possible. Functionality includes extracting tidy posterior summaries as in 'tidybayes' <https://github.com/mjskay/tidybayes>, estimating (average) treatment effects, common support calculations, and plotting useful summaries of these.
	"""
	
	homepage = "https://github.com/bonStats/tidytreatment"
	cran = "tidytreatment" 

	version("0.2.2", md5="22879a810d8b5aaab588676f82d7d252")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-tidybayes", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
