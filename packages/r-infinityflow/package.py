# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInfinityflow(RPackage):
	"""Augmenting Massively Parallel Cytometry Experiments Using Multivariate Non-Linear Regressions

	Pipeline to analyze and merge data files produced by BioLegend's LEGENDScreen or BD Human Cell Surface Marker Screening Panel (BD Lyoplates).
	"""
	
	bioc = "infinityFlow" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/infinityFlow_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/infinityFlow/infinityFlow_1.12.0.tar.gz"]

	version("1.18.0", tag="RELEASE_3_21")
	version("1.12.0", sha256="aec5f37ad9a9a27f637aec584fbf5a9a83cccf7af0e38051ef506a217c58815c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-matlab", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
