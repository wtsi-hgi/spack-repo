# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultis(RPackage):
	"""Reconstruction of Clones from Integration Site Readouts and
Visualization

	Tools necessary to reconstruct clonal affiliations from
    temporally and/or spatially separated measurements of viral
    integration sites. For this means it utilizes correlations present
    in the relative readouts of the integration sites. Furthermore,
    facilities for filtering of the data and visualization of different
    steps in the pipeline are provided with the package.
	"""
	
	cran = "MultIS" 

	version("0.6.2", md5="2b9c843dfffc7e9244567ffdd67e01f7")

	depends_on("r-clvalid", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-clv", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ltm", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-powerlaw", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmutil", type=("build", "run"))
