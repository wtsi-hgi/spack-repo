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

	version("1.36.0", commit="f545d33d24b322aa3869f310bbfe6edbd5ae4c26")
	version("1.30.0", commit="361a0e921c883d77aff35c3c13a54f13d84a858e")

	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
