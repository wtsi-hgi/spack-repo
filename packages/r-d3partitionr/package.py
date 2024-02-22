# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RD3partitionr(RPackage):
	"""Interactive Charts of Nested and Hierarchical Data with 'D3.js'

	Builds interactive 'd3.js' hierarchical visualisation easily. D3partitionR makes it easy to build and customize sunburst, circle treemap, treemap, partition chart, ...
	"""
	
	cran = "D3partitionR" 

	version("0.5.0", md5="b81f5cb6546d5a2c359f3bee8f3c0b5d")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-functional", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-titanic", type=("build", "run"))
