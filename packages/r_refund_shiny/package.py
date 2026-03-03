# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRefundShiny(RPackage):
	"""Interactive Plotting for Functional Data Analyses

	Produces Shiny applications for different types of popular functional data analyses. The functional data analyses are implemented in the refund package, then refund.shiny reads in the refund object and implements an object-specific set of plots based on the object class using S3.
	"""
	
	cran = "refund.shiny" 

	version("1.0", md5="032e0cf0d2c56aa4a196facd739c3577")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-shiny@0.11:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-refund", type=("build", "run"))
