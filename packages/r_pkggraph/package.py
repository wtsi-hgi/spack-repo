# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkggraph(RPackage):
	"""A Consistent and Intuitive Platform to Explore the Dependencies
of Packages on the Comprehensive R Archive Network Like
Repositories

	Interactively explore various dependencies of a package(s) (on the Comprehensive R Archive Network Like repositories) and perform analysis using tidy philosophy. Most of the functions return a 'tibble' object (enhancement of 'dataframe') which can be used for further analysis. The package offers functions to produce 'network' and 'igraph' dependency graphs. The 'plot' method produces a static plot based on 'ggnetwork' and 'plotd3' function produces an interactive D3 plot based on 'networkD3'.
	"""
	
	homepage = "https://github.com/talegari/pkggraph"
	cran = "pkggraph" 

	version("0.2.3", md5="881927940178d015555d3eaecb34f6c8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggnetwork@0.5.1:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-curl@2.5:", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-htmltools@0.3.5:", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
	depends_on("r-intergraph@2.0.2:", type=("build", "run"))
	depends_on("r-matrix@1.2.10:", type=("build", "run"))
	depends_on("r-networkd3@0.4:", type=("build", "run"))
	depends_on("r-network@1.13:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-tibble@1.3:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
