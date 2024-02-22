# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcyjs(RPackage):
	"""Display and manipulate graphs in cytoscape.js

	Interactive viewing and exploration of graphs, connecting R to Cytoscape.js, using websockets.
	"""
	
	bioc = "RCyjs" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/RCyjs_2.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/RCyjs/RCyjs_2.24.0.tar.gz"]

	version("2.24.0", md5="b02526ea0ff36d61fdac395633bc4a4d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-browserviz@2.7.18:", type=("build", "run"))
	depends_on("r-graph@1.56:", type=("build", "run"))
	depends_on("r-httpuv@1.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
