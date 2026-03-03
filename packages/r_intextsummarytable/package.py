# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntextsummarytable(RPackage):
	"""Creation of in-Text Summary Table

	Creation of tables of summary statistics or counts for clinical data (for 'TLFs'). 
  These tables can be exported as in-text table (with the 'flextable' package) for a Clinical Study Report 
  (Word format) or a 'topline' presentation (PowerPoint format), 
  or as interactive table (with the 'DT' package) to an html document for clinical data review.
	"""
	
	homepage = "https://github.com/openanalytics/inTextSummaryTable"
	cran = "inTextSummaryTable" 

	version("3.3.2", md5="24144a7a56488c4592ded9e48f074bf7")
	version("3.3.1", md5="750f5d416538ef2b16ab3b68c531993e")

	depends_on("r-clinutils@0.1:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-flextable@0.5.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2@1.4:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
