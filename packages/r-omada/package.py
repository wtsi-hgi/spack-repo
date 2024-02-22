# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmada(RPackage):
	"""Machine learning tools for automated transcriptome clustering analysis

	Symptomatic heterogeneity in complex diseases reveals differences in molecular states that need to be investigated. However, selecting the numerous parameters of an exploratory clustering analysis in RNA profiling studies requires deep understanding of machine learning and extensive computational experimentation. Tools that assist with such decisions without prior field knowledge are nonexistent and further gene association analyses need to be performed independently. We have developed a suite of tools to automate these processes and make robust unsupervised clustering of transcriptomic data more accessible through automated machine learning based functions. The efficiency of each tool was tested with four datasets characterised by different expression signal strengths. Our toolkit’s decisions reflected the real number of stable partitions in datasets where the subgroups are discernible. Even in datasets with less clear biological distinctions, stable subgroups with different expression profiles and clinical associations were found.
	"""
	
	bioc = "omada" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/omada_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/omada/omada_1.4.0.tar.gz"]

	version("1.4.0", md5="d214fdb20c51cbce86bf1d34c59cb84b")

	depends_on("r-pdfcluster@1.0.3:", type=("build", "run"))
	depends_on("r-kernlab@0.9.29:", type=("build", "run"))
	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-fpc@2.2.9:", type=("build", "run"))
	depends_on("r-rcpp@1.0.7:", type=("build", "run"))
	depends_on("r-dicer@0.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-reshape@0.8.8:", type=("build", "run"))
	depends_on("r-genieclust@1.1.3:", type=("build", "run"))
	depends_on("r-clvalid@0.7:", type=("build", "run"))
	depends_on("r-glmnet@4.1.3:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
