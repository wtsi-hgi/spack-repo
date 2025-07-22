# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIfaa(RPackage):
	"""Robust Inference for Absolute Abundance in Microbiome Analysis

	This package offers a robust approach to make inference on the association of covariates with the absolute abundance (AA) of microbiome in an ecosystem. It can be also directly applied to relative abundance (RA) data to make inference on AA because the ratio of two RA is equal to the ratio of their AA. This algorithm can estimate and test the associations of interest while adjusting for potential confounders. The estimates of this method have easy interpretation like a typical regression analysis. High-dimensional covariates are handled with regularization and it is implemented by parallel computing. False discovery rate is automatically controlled by this approach. Zeros do not need to be imputed by a positive value for the analysis. The IFAA package also offers the 'MZILN' function for estimating and testing associations of abundance ratios with covariates.
	"""
	
	homepage = "https://pubmed.ncbi.nlm.nih.gov/35241863/"
	bioc = "IFAA"

	version("1.10.0", commit="3d93d6ff8cc0b7d4f445bd524a0d19b7367ab680")
	version("1.4.0", commit="ca5c2f7c8cc635ce07642f612b5da16228a8643a")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-foreach@1.4.3:", type=("build", "run"))
	depends_on("r-matrix@1.4.0:", type=("build", "run"))
	depends_on("r-hdci@1.0.2:", type=("build", "run"))
	depends_on("r-doparallel@1.0.11:", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-matrixextra", type=("build", "run"))
