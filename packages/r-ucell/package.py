# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUcell(RPackage):
	"""Rank-based signature enrichment analysis for single-cell data

	UCell is a package for evaluating gene signatures in single-cell datasets. UCell signature scores, based on the Mann-Whitney U statistic, are robust to dataset size and heterogeneity, and their calculation demands less computing time and memory than other available methods, enabling the processing of large datasets in a few minutes even on machines with limited computing power. UCell can be applied to any single-cell data matrix, and includes functions to directly interact with SingleCellExperiment and Seurat objects.
	"""
	
	homepage = "https://github.com/carmonalab/UCell"
	bioc = "UCell" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/UCell_2.6.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/UCell/UCell_2.6.2.tar.gz"]

	version("2.6.2", sha256="ad8c56756ac2645f02cfbb00e6aec756528ebc729413ba9af57ff8e3425a6403")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-data-table@1.13.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biocneighbors", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
