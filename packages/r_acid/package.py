# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcid(RPackage):
	"""Analysing Conditional Income Distributions

	Functions for the analysis of income distributions for subgroups of the population as defined by a set of variables like age, gender, region, etc. This entails a Kolmogorov-Smirnov test for a mixture distribution as well as functions for moments, inequality measures, entropy measures and polarisation measures of income distributions. This package thus aides the analysis of income inequality by offering tools for the exploratory analysis of income distributions at the disaggregated level. 
	"""
	
	cran = "acid" 

	version("1.1", md5="bd22d1cd6a58a7d7340680a066935b37")

	depends_on("r-gamlss", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
