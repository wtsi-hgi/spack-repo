# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRppanalyzer(RPackage):
	"""Reads, Annotates, and Normalizes Reverse Phase Protein Array
Data

	Reads in sample description and slide description files and
        annotates the expression values taken from GenePix results files
	(text file format used by many microarray scanner and software providers). 
	After normalization data can be visualized as boxplot, heatmap or dotplot.
	"""
	
	cran = "RPPanalyzer" 

	version("1.4.9", md5="8def3c9eaf30d69966c05a5d4a364caf")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-gam", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
