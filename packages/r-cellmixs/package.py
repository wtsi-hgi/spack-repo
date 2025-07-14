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

	version("1.24.0", commit="c53e6c455ca3745e69f160bb89fbc8285d326aba")
	version("1.18.0", commit="f781a7ccd8d7d8ee2a248591a3f0a68a2deb31e1")

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
