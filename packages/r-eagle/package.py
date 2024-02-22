# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REagle(RPackage):
	"""Multiple Locus Association Mapping on a Genome-Wide Scale

	An implementation of multiple-locus association mapping on a genome-wide scale. 'Eagle' can handle inbred and  outbred study populations, populations of arbitrary unknown complexity, and data larger than the memory capacity of the computer. Since 'Eagle' is based on linear mixed models, it is best suited to the analysis of data on continuous traits. However, it can tolerate non-normal data. 'Eagle' reports, as its findings, the best set of snp in strongest association with a trait. For users unfamiliar with R, to perform an analysis, run 'OpenGUI()'. This  opens a web browser to the menu-driven user interface for the input of data, and for performing genome-wide analysis.
	"""
	
	homepage = "http://eagle.r-forge.r-project.org"
	cran = "Eagle" 

	version("2.5", md5="00169dbeac1584ceb540daadbf55ddbd")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-mmap", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-fontawesome", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
