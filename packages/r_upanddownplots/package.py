# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUpanddownplots(RPackage):
	"""Displays Percentage and Absolute Changes

	Displays percentage changes by height and absolute changes by area for up to three nested or non-nested levels. The plots visualise changes in indices and markets, showing how the changes for sectors or for individual components contribute to the overall change. Data can be classified by up to three levels of grouping variables in a layered, hierarchical plot. Each level can be ordered in several ways including by baseline, by percentage change, and by absolute change. The vignettes give examples.
	"""
	
	cran = "UpAndDownPlots" 

	version("0.5.0", md5="23fe3915c32a17f1d1861c299fddfff3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
