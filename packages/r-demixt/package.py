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

	version("1.24.0", commit="e25636b21480789f17f0c7fb339dc66d0fde65c3")
	version("1.18.0", commit="27c62df4672bd06b688fb69a1399d2cfd3bf188d")

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
