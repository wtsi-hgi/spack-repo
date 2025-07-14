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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RnaSeqSampleSize_2.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RnaSeqSampleSize/RnaSeqSampleSize_2.12.0.tar.gz"]

    version("2.18.0", tag="RELEASE_3_21")
	version("2.12.0", sha256="f87cc4422898866c086e35a5629d70c97bde1d4e82c8823421f00b00b0e607b0")

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
