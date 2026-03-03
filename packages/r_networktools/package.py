# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetworktools(RPackage):
	"""Tools for Identifying Important Nodes in Networks

	Includes assorted tools for network analysis. Bridge centrality; goldbricker; MDS, PCA, & eigenmodel network plotting.
	"""
	
	homepage = "https://CRAN.R-project.org/package=networktools"
	cran = "networktools" 

	version("1.5.2", md5="04a42c50ca01e17cdedda1292f53d12e")
	version("1.5.1", md5="5ef9be75430e6a95adc25d10534bfbe7")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-cocor", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-eigenmodel", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-smacof", type=("build", "run"))
	depends_on("r-wordcloud", type=("build", "run"))
