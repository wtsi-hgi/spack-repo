# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCatdyn(RPackage):
	"""Fishery Stock Assessment by Catch Dynamics Models

	Based on fishery Catch Dynamics instead of fish Population Dynamics (hence CatDyn) and using high-frequency or medium-frequency catch in biomass or numbers, fishing nominal effort, and mean fish body weight by time step, from one or two fishing fleets, estimate stock abundance, natural mortality rate, and fishing operational parameters. It includes methods for data organization, plotting standard exploratory and analytical plots, predictions, for 100 types of models of increasing complexity, and 72 likelihood models for the data.
	"""
	
	cran = "CatDyn" 

	version("1.1-1", md5="2f7efe707e2e150cb7f8ea0fe60e1af5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-optimx@2013.8.6:", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
