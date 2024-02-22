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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/RGraph2js_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/RGraph2js/RGraph2js_1.30.0.tar.gz"]

	version("1.30.0", md5="ccb2f26623270911ba855aa97e1269e1")

	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
