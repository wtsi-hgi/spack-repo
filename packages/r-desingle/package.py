# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDesingle(RPackage):
	"""DEsingle for detecting three types of differential expression in single-cell RNA-seq data

	DEsingle is an R package for differential expression (DE) analysis of single-cell RNA-seq (scRNA-seq) data. It defines and detects 3 types of differentially expressed genes between two groups of single cells, with regard to different expression status (DEs), differential expression abundance (DEa), and general differential expression (DEg). DEsingle employs Zero-Inflated Negative Binomial model to estimate the proportion of real and dropout zeros and to define and detect the 3 types of DE genes. Results showed that DEsingle outperforms existing methods for scRNA-seq DE analysis, and can reveal different types of DE genes that are enriched in different biological functions.
	"""
	
	homepage = "https://miaozhun.github.io/DEsingle/"
	bioc = "DEsingle"

	version("1.28.0", commit="6a268cdd8c5da1ee2a0dbcceda8698b3d6168c65")
	version("1.22.0", commit="dabeba9eaacc691d0e887c63c1173a37e3616a6b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-matrix@1.2.14:", type=("build", "run"))
	depends_on("r-mass@7.3.45:", type=("build", "run"))
	depends_on("r-vgam@1.0.2:", type=("build", "run"))
	depends_on("r-bbmle@1.0.18:", type=("build", "run"))
	depends_on("r-gamlss@4.4.0:", type=("build", "run"))
	depends_on("r-maxlik@1.3.4:", type=("build", "run"))
	depends_on("r-pscl@1.4.9:", type=("build", "run"))
	depends_on("r-biocparallel@1.12:", type=("build", "run"))
