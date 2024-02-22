# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForestmodel(RPackage):
	"""Forest Plots from Regression Models

	Produces forest plots using 'ggplot2' from models produced by functions
    such as stats::lm(), stats::glm() and survival::coxph().
	"""
	
	cran = "forestmodel" 

	version("0.6.2", md5="30ba10e33f53eebd9590b053e93a19eb")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-broom@0.5:", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-tibble@1.4.2:", type=("build", "run"))
