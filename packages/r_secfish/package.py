# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSecfish(RPackage):
	"""Disaggregate Variable Costs

	These functions were developed within SECFISH project (Strengthening regional cooperation in the area of fisheries  data collection-Socio-economic data collection for fisheries, aquaculture and the processing industry at EU level). They are aimed at identifying  correlations between costs and transversal variables by metier using individual vessel data and for disaggregating variable costs from  fleet segment to metier  level.  
	"""
	
	cran = "SECFISH" 

	version("0.1.7", md5="4d4c905bea8b9d09772cfcee21d7f7f1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-optimization", type=("build", "run"))
