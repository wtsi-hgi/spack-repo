# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRavenr(RPackage):
	"""Raven Hydrological Modelling Framework R Support and Analysis

	Utilities for processing input and output files associated with the Raven Hydrological Modelling Framework. Includes various plotting functions, model diagnostics, reading output files into extensible time series format, and support for writing Raven input files. 
    The 'RavenR' package is also archived at Chlumsky et al. (2020) <doi:10.5281/zenodo.4248183>.
    The Raven Hydrologic Modelling Framework method can be referenced with Craig et al. (2020) <doi:10.1016/j.envsoft.2020.104728>.
	"""
	
	homepage = "https://github.com/rchlumsk/RavenR"
	cran = "RavenR" 

	version("2.2.0", md5="7a0dc119a92d90e349e9274811879440")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dygraphs", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
