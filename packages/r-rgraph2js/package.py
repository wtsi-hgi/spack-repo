# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgraph2js(RPackage):
	"""Convert a Graph into a D3js Script

	Generator of web pages which display interactive network/graph visualizations with D3js, jQuery and Raphael.
	"""
	
	bioc = "RGraph2js" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RGraph2js_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RGraph2js/RGraph2js_1.30.0.tar.gz"]

    version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="8c8d1f5d86d5057f2e0206c1b744a858939d6a19d5cea3f01d7d69785d760d30")

	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
