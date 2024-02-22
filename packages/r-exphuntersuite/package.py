# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExphuntersuite(RPackage):
	"""Package For The Comprehensive Analysis Of Transcriptomic Data

	The ExpHunterSuite implements a comprehensive protocol for the analysis of transcriptional data using established *R* packages and combining their results. It covers all key steps in DEG detection, CEG detection and functional analysis for RNA-seq data. It has been implemented as an R package containing functions that can be run interactively. In addition, it also contains scripts that wrap the functions and can be run directly from the command line.
	"""
	
	bioc = "ExpHunterSuite" 
	urls = ["https://www.bioconductor.org/packages/release/workflows/src/contrib/ExpHunterSuite_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/workflows/src/contrib/Archive/ExpHunterSuite/ExpHunterSuite_1.10.0.tar.gz"]

	version("1.10.0", md5="84adeeade381f26a12e2bdd69208e352")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-reactomepa", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-noiseq", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-topgo", type=("build", "run"))
	depends_on("r-diffcoexp", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-enrichplot", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-mirbaseversions-db", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-mkinfer", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-ggupset", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-dose", type=("build", "run"))
	depends_on("r-heatmaply", type=("build", "run"))
	depends_on("r-enhancedvolcano", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-tximport", type=("build", "run"))
	depends_on("r-annotatr", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-factoinvestigate", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))

	# workflow