# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRada(RPackage):
	"""Statistical Analysis and Cut-Point Determination of Immunoassays

	Systematically transform immunoassay data, evaluate if the data is normally distributed, and pick the right method for cut point determination based on that evaluation. This package can also produce plots that are needed for reports, so data analysis and visualization can be done easily.
	"""
	
	cran = "rADA" 

	version("1.1.9", md5="d2376e6fc7d054d10cee9ae912f95839")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lme4@1.1.21:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-matrixstats@0.56:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-lmertest@3.1:", type=("build", "run"))
	depends_on("r-e1071@1.7.2:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-hmisc@4.3:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-forestplot@1.10:", type=("build", "run"))
	depends_on("r-knitr@1.29:", type=("build", "run"))
	depends_on("r-openxlsx@4.2.2:", type=("build", "run"))
	depends_on("r-car@3:", type=("build", "run"))
