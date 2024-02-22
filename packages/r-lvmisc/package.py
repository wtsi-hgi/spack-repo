# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLvmisc(RPackage):
	"""Veras Miscellaneous

	Contains a collection of useful
    functions for basic data computation and manipulation,
    wrapper functions for generating 'ggplot2' graphics,
    including statistical model diagnostic plots, methods
    for computing statistical models quality measures (such
    as AIC, BIC, r squared, root mean squared error) and
    general utilities.
	"""
	
	homepage = "https://lveras.com/lvmisc/"
	cran = "lvmisc" 

	version("0.1.2", md5="ee2a18c63abd67c95ecaf3050d76e560")

	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@0.4.6:", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vctrs@0.3:", type=("build", "run"))
