# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiomass(RPackage):
	"""Estimating Aboveground Biomass and Its Uncertainty in Tropical
Forests

	Contains functions to estimate aboveground biomass/carbon and its uncertainty in tropical forests. 
	These functions allow to (1) retrieve and to correct taxonomy, (2) estimate wood density and its uncertainty, 
	(3) construct height-diameter models, (4) manage tree and plot coordinates, 
	(5) estimate the aboveground biomass/carbon at the stand level with associated uncertainty. 
	To cite 'BIOMASS', please use citation("BIOMASS"). 
	See more in the article of Réjou-Méchain et al. (2017) <doi:10.1111/2041-210X.12753>.
	"""
	
	homepage = "https://github.com/umr-amap/BIOMASS"
	cran = "BIOMASS" 

	version("2.1.11", md5="664201262573ad0d9de4eb3e631b8996")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-proj4", type=("build", "run"))
	depends_on("r-data-table@1.9.8:", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
