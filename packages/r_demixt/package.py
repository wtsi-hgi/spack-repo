# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDemixt(RPackage):
	"""Cell type-specific deconvolution of heterogeneous tumor samples with two or three components using expression data from RNAseq or microarray platforms

	DeMixT is a software package that performs deconvolution on transcriptome data from a mixture of two or three components.
	"""
	
	bioc = "DeMixT" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DeMixT_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DeMixT/DeMixT_1.18.0.tar.gz"]

	version("1.18.0", md5="7d2e6439b9eb756f3f9e8a6a3c206d4e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-dss", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-truncdist", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
