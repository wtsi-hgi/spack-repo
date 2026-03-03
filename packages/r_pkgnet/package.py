# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkgnet(RPackage):
	"""Get Network Representation of an R Package

	Tools from the domain of graph theory can be used to quantify the complexity
             and vulnerability to failure of a software package. That is the guiding philosophy
             of this package. 'pkgnet' provides tools to analyze the dependencies between functions
             in an R package and between its imported packages.  See the pkgnet website for vignettes 
             and other supplementary information.
	"""
	
	homepage = "https://github.com/uptake/pkgnet"
	cran = "pkgnet" 

	version("0.4.2", md5="97d01845b3001815ad1fbc8207da645e")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-covr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown@1.9:", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
