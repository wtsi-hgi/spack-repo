# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnvscope(RPackage):
	"""A Versatile Toolkit for Copy Number Variation Relationship Data
Analysis and Visualization

	Provides the ability to create interaction maps, discover CNV map domains (edges), gene annotate interactions, and create interactive visualizations of these CNV interaction maps.
	"""
	
	homepage = "https://github.com/jamesdalg/CNVScope/"
	cran = "CNVScope" 

	version("3.7.2", md5="4871f5751e18cb3ffbf7d31ca359bb11")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-jointseg", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-genomicinteractions", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-openimager", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
