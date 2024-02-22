# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGuilds(RPackage):
	"""Implementation of Sampling Formulas for the Unified Neutral
Model of Biodiversity and Biogeography, with or without Guild
Structure

	A collection of sampling formulas for the unified neutral model of biogeography and biodiversity. Alongside the sampling formulas, it includes methods to perform maximum likelihood optimization of the sampling formulas, methods to generate data given the neutral model, and methods to estimate the expected species abundance distribution. Sampling formulas included in the GUILDS package are the Etienne Sampling Formula (Etienne 2005), the guild sampling formula, where guilds are assumed to differ in dispersal ability (Janzen et al. 2015), and  the guilds sampling formula conditioned on guild size (Janzen et al. 2015).
	"""
	
	homepage = "https://github.com/thijsjanzen/GUILDS"
	cran = "GUILDS" 

	version("1.4.6", md5="123f59a57d0b97347ae4e1ce1d9b7d1a")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
