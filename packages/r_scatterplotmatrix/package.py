# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScatterplotmatrix(RPackage):
	"""'Htmlwidget' for a Scatter Plot Matrix

	Create a scatter plot matrix, using 'htmlwidgets' package and 'd3.js'.
	"""
	
	homepage = "https://ifpen.gitlabfr.com/detocs/scatterplotmatrix"
	cran = "scatterPlotMatrix" 

	version("0.2.0", md5="a9d0491f231e11c048c0a9a189b44252")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
