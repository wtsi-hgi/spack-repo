# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarr(RPackage):
	"""Maximum rank reproducibility

	marr (Maximum Rank Reproducibility) is a nonparametric approach that detects reproducible signals using a maximal rank statistic for high-dimensional biological data. In this R package, we implement functions that measures the reproducibility of features per sample pair and sample pairs per feature in high-dimensional biological replicate experiments. The user-friendly plot functions in this package also plot histograms of the reproducibility of features per sample pair and sample pairs per feature. Furthermore, our approach also allows the users to select optimal filtering threshold values for the identification of reproducible features and sample pairs based on output visualization checks (histograms). This package also provides the subset of data filtered by reproducible features and/or sample pairs.
	"""
	
	bioc = "marr" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/marr_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/marr/marr_1.12.0.tar.gz"]

	version("1.12.0", md5="3b839d77065c34ddb5f5c2a8eee277ea")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
