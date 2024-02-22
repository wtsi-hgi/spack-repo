# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScrnatools(RPackage):
	"""Single Cell RNA Sequencing Data Analysis Tools

	We integrated the common analysis methods utilized in single cell RNA sequencing data, which included cluster method, principal components analysis (PCA), the filter of differentially expressed genes, pathway enrichment analysis and correlated analysis methods.
	"""
	
	cran = "scRNAtools" 

	version("1.0", md5="694fc3fa8ea098c453c13653d3528194")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-all", type=("build", "run"))
	depends_on("r-consensusclusterplus", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-tpea", type=("build", "run"))
	depends_on("r-rmisc", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-performanceanalytics", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
