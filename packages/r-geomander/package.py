# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeomander(RPackage):
	"""Geographic Tools for Studying Gerrymandering

	A compilation of tools to complete common tasks for studying gerrymandering. 
    This focuses on the geographic tool side of common problems, such as linking 
    different levels of spatial units or estimating how to break up units. Functions 
    exist for creating redistricting-focused data for the US.
	"""
	
	homepage = "https://christophertkenny.com/geomander/"
	cran = "geomander" 

	version("2.3.0", md5="a08edc06c0e15bd3d58ceea9898077f3")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-censable", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dataverse", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-geos", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpp@1.0.7:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tinytiger", type=("build", "run"))
