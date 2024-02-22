# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSchex(RPackage):
	"""Hexbin plots for single cell omics data

	Builds hexbin plots for variables and dimension reduction stored in single cell omics data such as SingleCellExperiment and SeuratObject. The ideas used in this package are based on the excellent work of Dan Carr, Nicholas Lewin-Koh, Martin Maechler and Thomas Lumley.
	"""
	
	homepage = "https://github.com/SaskiaFreytag/schex"
	bioc = "schex" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/schex_1.16.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/schex/schex_1.16.1.tar.gz"]

	version("1.16.1", md5="f57d8e86734da9d7e2b645c5871fa7a1")

	depends_on("r-singlecellexperiment@1.7.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-concaveman", type=("build", "run"))
