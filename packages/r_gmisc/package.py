# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmisc(RPackage):
	"""Descriptive Statistics, Transition Plots, and More

	Tools for making the descriptive "Table 1" used in medical
    articles, a transition plot for showing changes between categories
    (also known as a Sankey diagram), flow charts by extending the grid package,
    a method for variable selection based on the SVD, Bézier lines with arrows
    complementing the ones in the 'grid' package, and more.
	"""
	
	homepage = "https://gforge.se"
	cran = "Gmisc" 

	version("3.0.3", md5="4e146b2852f4da1a80fa8bfcc31c5258")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-htmltable@2:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-forestplot", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
