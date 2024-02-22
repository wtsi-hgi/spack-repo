# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaffle(RPackage):
	"""Create Waffle Chart Visualizations

	Square pie charts (a.k.a. waffle charts) can be used
    to communicate parts of a whole for categorical quantities. To emulate the
    percentage view of a pie chart, a 10x10 grid should be used with each square
    representing 1% of the total. Modern uses of waffle charts do not
    necessarily adhere to this rule and can be created with a grid of any
    rectangular shape. Best practices suggest keeping the number of categories
    small, just as should be done when creating pie charts. Tools are provided
    to create waffle charts as well as stitch them together, and to use glyphs
    for making isotype pictograms.
	"""
	
	cran = "waffle" 

	version("1.0.2", md5="5d8baee6c96eb2a1e7b8001ef159f45e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-extrafont", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
