# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVariancepartition(RPackage):
	"""Quantify and interpret drivers of variation in multilevel gene expression experiments

	Quantify and interpret multiple sources of biological and technical variation in gene expression experiments. Uses a linear mixed model to quantify variation in gene expression attributable to individual, tissue, time point, or technical variables.  Includes dream differential expression analysis for repeated measures.
	"""
	
	homepage = "http://bioconductor.org/packages/variancePartition"
	bioc = "variancePartition" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/variancePartition_1.32.5.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/variancePartition/variancePartition_1.32.5.tar.gz"]

    version("1.38.0", tag="RELEASE_3_21")
	version("1.32.5", md5="cd02e6e3024f4f5bbb5d8c1dcb471d15")
	version("1.24.1", md5="922a5518ac302be34b1e416772190db5", url="https://www.bioconductor.org/packages/3.14/bioc/src/contrib/variancePartition_1.24.1.tar.gz")

	depends_on("r@4.3:", type=("build", "run"), when="@1.32.5:")
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pbkrtest@0.4.4:", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-matrix@1.4:", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"), when="@1.32.5:")
	depends_on("r-matrixstats", type=("build", "run"), when="@1.32.5:")
	depends_on("r-rhpcblasctl", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-remacor@0.0.15:", type=("build", "run"), when="@1.32.5:")
	depends_on("r-fancova", type=("build", "run"), when="@1.32.5:")
	depends_on("r-aod", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lme4@1.1.33:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"), when="@:1.30")
	depends_on("r-doparallel", type=("build", "run"), when="@:1.30")
	depends_on("r-progress", type=("build", "run"), when="@:1.30")
