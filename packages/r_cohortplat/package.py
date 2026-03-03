# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCohortplat(RPackage):
	"""Simulation of Cohort Platform Trials for Combination Treatments

	A collection of functions dedicated to simulating staggered entry platform 
    trials whereby the treatment under investigation is a combination of two 
    active compounds. In order to obtain approval for this combination therapy,
    superiority of the combination over the two active compounds and superiority
    of the two active compounds over placebo need to be demonstrated. 
    A more detailed description of the design can be found in 
    Meyer et al. <DOI:10.1002/pst.2194> and a manual in Meyer et al. <arXiv:2202.02182>.
	"""
	
	cran = "CohortPlat" 

	version("1.0.5", md5="5c5ad0f8a25fd09be91f923810c285d3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-epitools", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
