# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialpop(RPackage):
	"""Generation of Spatial Data with Spatially Varying Model
Parameter

	A spatial population can be generated based on spatially varying regression model under the assumption that observations are collected from a uniform two-dimensional grid consist of (m * m) lattice points with unit distance between any two neighbouring points. For method details see Chao, Liu., Chuanhua, Wei. and Yunan, Su. (2018).<DOI:10.1080/10485252.2018.1499907>.  This spatially generated data can be used to test different issues related to the statistical analysis of spatial data.
 This generated spatial data can be utilized in geographically weighted regression analysis for studying the spatially varying relationships among the variables.
	"""
	
	cran = "SpatialPOP" 

	version("0.1.0", md5="d7221a84b8e4d2a06c88b53bb7081c95")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
	depends_on("r-numbers", type=("build", "run"))
