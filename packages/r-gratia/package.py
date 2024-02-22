# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGratia(RPackage):
	"""Graceful 'ggplot'-Based Graphics and Other Functions for GAMs
Fitted Using 'mgcv'

	Graceful 'ggplot'-based graphics and utility functions for working with generalized additive models (GAMs) fitted using the 'mgcv' package. Provides a reimplementation of the plot() method for GAMs that 'mgcv' provides, as well as 'tidyverse' compatible representations of estimated smooths.
	"""
	
	homepage = "https://gavinsimpson.github.io/gratia/"
	cran = "gratia" 

	version("0.8.2", md5="7aaf3cfd14c163bebf9edcedcff28ee6")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-mgcv@1.8.41:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-mvnfast", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
