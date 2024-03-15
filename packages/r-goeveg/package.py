# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoeveg(RPackage):
	"""Functions for Community Data and Ordinations

	A collection of functions useful in (vegetation) community analyses and ordinations. Includes automatic species selection for ordination diagrams, NMDS stress/scree plots, species response curves, merging of taxa as well as calculation and sorting of synoptic tables.
	"""
	
	homepage = "https://github.com/fvlampe/goeveg/"
	cran = "goeveg" 

	version("0.7.4", md5="1046f415585cc857d03788ccb89719b2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
