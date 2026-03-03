# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenrepgrid(RPackage):
	"""Tools to Analyze Repertory Grid Data

	Analyze repertory grids, a qualitative-quantitative 
    data collection technique devised by George A. Kelly in the 1950s. Today, grids are used across 
    various domains ranging from clinical psychology to marketing. The package contains
    functions to quantitatively analyze and visualize repertory grid data.
	"""
	
	homepage = "https://github.com/markheckmann/OpenRepGrid"
	cran = "OpenRepGrid" 

	version("0.1.14", md5="1197b243aa13599e754f9575bc5f6a9a")

	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-pvclust", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
