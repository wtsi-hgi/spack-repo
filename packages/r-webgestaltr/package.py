# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWebgestaltr(RPackage):
	"""Gene Set Analysis Toolkit WebGestaltR

	The web version WebGestalt <https://www.webgestalt.org> supports 12 organisms, 354 gene identifiers and 321,251 function categories. Users can upload the data and functional categories with their own gene identifiers. In addition to the Over-Representation Analysis, WebGestalt also supports Gene Set Enrichment Analysis and Network Topology Analysis. The user-friendly output report allows interactive and efficient exploration of enrichment results. The WebGestaltR package not only supports all above functions but also can be integrated into other pipeline or simultaneously analyze multiple gene lists.
	"""
	
	homepage = "https://github.com/bzhanglab/WebGestaltR"
	cran = "WebGestaltR" 

	version("0.4.6", md5="3f536127bb2066b5ed8461f5e249fa76")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-doparallel@1.0.10:", type=("build", "run"))
	depends_on("r-foreach@1.4:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-svglite", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-apcluster", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
