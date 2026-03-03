# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGridsampler(RPackage):
	"""A Simulation Tool to Determine the Required Sample Size for
Repertory Grid Studies

	Simulation tool to facilitate determination of
    required sample size to achieve category saturation
    for studies using multiple repertory grids in conjunction with
    content analysis.
	"""
	
	homepage = "https://github.com/markheckmann/gridsampler"
	cran = "gridsampler" 

	version("0.6", md5="69f335a92728bf588d88b3c12649a796")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-biasedurn", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
