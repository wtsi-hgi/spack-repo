# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSfislands(RPackage):
	"""Streamlines the Process of Fitting Areal Spatial Models

	Helpers for addressing the issue of disconnected spatial units. 
    It allows for convenient adding and removal of neighbourhood connectivity between areal units prior to modelling, with the visual aid of maps.
    Post-modelling, it reduces the human workload for extracting, tidying and mapping predictions from areal models.
	"""
	
	homepage = "https://github.com/horankev/sfislands"
	cran = "sfislands" 

	version("1.0.0", md5="df33fe7dd7d877031728f4c3bea02315")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-broom-mixed", type=("build", "run"))
