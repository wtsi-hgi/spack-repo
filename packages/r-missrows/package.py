# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMissrows(RPackage):
	"""Handling Missing Individuals in Multi-Omics Data Integration

	The missRows package implements the MI-MFA method to deal with missing individuals ('biological units') in multi-omics data integration. The MI-MFA method generates multiple imputed datasets from a Multiple Factor Analysis model, then the yield results are combined in a single consensus solution. The package provides functions for estimating coordinates of individuals and variables, imputing missing individuals, and various diagnostic plots to inspect the pattern of missingness and visualize the uncertainty due to missing values.
	"""
	
	bioc = "missRows" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/missRows_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/missRows/missRows_1.22.0.tar.gz"]

	version("1.28.0", tag="RELEASE_3_21")
	version("1.22.0", sha256="fe4a4c0cf8d8b07c8dd0d8f5ac85e44dd0a0b701a6ed36e25992ed6ea2fbae8f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
