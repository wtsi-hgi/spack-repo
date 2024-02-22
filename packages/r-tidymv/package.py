# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidymv(RPackage):
	"""Tidy Model Visualisation for Generalised Additive Models

	Provides functions for visualising generalised
    additive models and getting predicted values using tidy tools from the 'tidyverse' packages.
	"""
	
	homepage = "https://github.com/stefanocoretta/tidymv"
	cran = "tidymv" 

	version("3.4.2", md5="e0db3d683124f3ee440b6e6b1d41beb5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
