# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellmixs(RPackage):
	"""Evaluate Cellspecific Mixing

	CellMixS provides metrics and functions to evaluate batch effects, data integration and batch effect correction in single cell trancriptome data with single cell resolution. Results can be visualized and summarised on different levels, e.g. on cell, celltype or dataset level.
	"""
	
	homepage = "https://github.com/almutlue/CellMixS"
	bioc = "CellMixS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CellMixS_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CellMixS/CellMixS_1.18.0.tar.gz"]

	version("1.18.0", sha256="e416a21a70a23da7cca4d67f2e594037b26cee69ef5e51a2ce9f9a3421ec3536")

	depends_on("r-ksamples", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biocneighbors", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scater", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
