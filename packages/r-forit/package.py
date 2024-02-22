# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForit(RPackage):
	"""Functions to Estimate Tree Volume and Phytomass in the Italian
Forest Inventory 2005

	Tabacchi et al. (2011) published a very detailed study producing a uniform system of functions to estimate tree volume and
    phytomass components (stem, branches, stool). The estimates of the 2005 Italian forest inventory (<https://www.inventarioforestale.org/it/>) 
    are based on these functions. The study documents the domain of applicability of each function and the equations to quantify estimates
    accuracies for individual estimates as well as for aggregated estimates. This package makes the functions available in the R environment. 
    Version 2 exposes two distinct functions for individual and summary estimates. To facilitate access to the functions, tree species 
    identification is now based on EPPO species codes (<https://data.eppo.int/>).
	"""
	
	homepage = "https://gitlab.com/NuoroForestrySchool/ForIT.git"
	cran = "ForIT" 

	version("2.4.0", md5="5a1f95857199fffdd3d4decb5f3a015d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-metr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
