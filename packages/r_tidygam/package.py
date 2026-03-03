# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidygam(RPackage):
	"""Tidy Prediction and Plotting of Generalised Additive Models

	Provides functions that compute predictions from Generalised
    Additive Models (GAMs) fitted with 'mgcv' and return them as a tibble.
    These can be plotted with a generic plot()-method that uses 'ggplot2' or
    plotted as any other data frame. The main function is predict_gam().
	"""
	
	homepage = "https://github.com/stefanocoretta/tidygam"
	cran = "tidygam" 

	version("0.2.0", md5="1dc395fa4cdd05a8f74749422814b32e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-insight", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
