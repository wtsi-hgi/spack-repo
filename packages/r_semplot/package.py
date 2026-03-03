# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemplot(RPackage):
	"""Path Diagrams and Visual Analysis of Various SEM Packages'
Output

	Path diagrams and visual analysis of various SEM packages' output.
	"""
	
	homepage = "https://github.com/SachaEpskamp/semPlot"
	cran = "semPlot" 

	version("1.1.6", md5="65ff44f7ee97e862a8e9a986a4e305d1")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-qgraph@1.2.4:", type=("build", "run"))
	depends_on("r-lavaan@0.5.11:", type=("build", "run"))
	depends_on("r-sem@3.1.0:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-igraph@0.6.3:", type=("build", "run"))
	depends_on("r-lisreltor", type=("build", "run"))
	depends_on("r-rockchalk", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-openmx", type=("build", "run"))
