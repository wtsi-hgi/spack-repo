# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnaseqsamplesize(RPackage):
	"""RnaSeqSampleSize

	RnaSeqSampleSize package provides a sample size calculation method based on negative binomial model and the exact test for assessing differential expression analysis of RNA-seq data. It controls FDR for multiple testing and utilizes the average read count and dispersion distributions from real data to estimate a more reliable sample size. It is also equipped with several unique features, including estimation for interested genes or pathway, power curve visualization, and parameter optimization.
	"""
	
	bioc = "RnaSeqSampleSize" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/RnaSeqSampleSize_2.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/RnaSeqSampleSize/RnaSeqSampleSize_2.12.0.tar.gz"]

	version("2.12.0", md5="faa40e62b53c345d9298c32310e6488c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rnaseqsamplesizedata", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-heatmap3", type=("build", "run"))
	depends_on("r-matlab", type=("build", "run"))
	depends_on("r-keggrest", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-recount", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
