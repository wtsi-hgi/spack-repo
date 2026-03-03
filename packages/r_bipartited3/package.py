# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBipartited3(RPackage):
	"""Interactive Bipartite Graphs

	Generates interactive bipartite graphs using the D3 library.
    Designed for use with the 'bipartite' analysis package.
    Sources open source 'viz-js' library 
    Adapted from examples at <https://bl.ocks.org/NPashaP> (released under GPL-3).
	"""
	
	cran = "bipartiteD3" 

	version("0.3.0", md5="cfc1b3b54f3d73d073f4d6f61874edb0", url="https://cran.r-project.org/src/contrib/bipartiteD3_0.3.0.tar.gz")

	depends_on("r-rcolorbrewer@1.1:", type=("build", "run"))
	depends_on("r-r2d3@0.2.2:", type=("build", "run"))
	depends_on("r-purrr@0.2.5:", type=("build", "run"))
	depends_on("r-dplyr@0.7.5:", type=("build", "run"))
	depends_on("r-tidyr@0.8:", type=("build", "run"))
	depends_on("r-stringr@1.3:", type=("build", "run"))
	depends_on("r-tibble@1.4:", type=("build", "run"))
	depends_on("r-downloader@0.4:", type=("build", "run"))
