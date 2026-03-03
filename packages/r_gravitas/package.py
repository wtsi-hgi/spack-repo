# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGravitas(RPackage):
	"""Explore Probability Distributions for Bivariate Temporal
Granularities

	Provides tools for systematically exploring large quantities of 
             temporal data across cyclic temporal granularities
             (deconstructions of time) by visualizing probability distributions.
             Cyclic time granularities can be circular, quasi-circular or 
             aperiodic. 'gravitas' computes cyclic
             single-order-up or multiple-order-up granularities, check the
             feasibility of creating plots for any two cyclic granularities
             and recommend probability distributions plots for exploring
             periodicity in the data.
	"""
	
	homepage = "https://github.com/Sayani07/gravitas/"
	cran = "gravitas" 

	version("0.1.3", md5="ca9895b981119119626afc57bc7da67a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-tsibble@0.8:", type=("build", "run"))
	depends_on("r-tibble@2.1.1:", type=("build", "run"))
	depends_on("r-rlang@0.3.4:", type=("build", "run"))
	depends_on("r-tidyr@0.8.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.1.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-lvplot", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ineq", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
