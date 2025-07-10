# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidysinglecellexperiment(RPackage):
	"""Brings SingleCellExperiment to the Tidyverse

	'tidySingleCellExperiment' is an adapter that abstracts the 'SingleCellExperiment' container in the form of a 'tibble'. This allows *tidy* data manipulation, nesting, and plotting. For example, a 'tidySingleCellExperiment' is directly compatible with functions from 'tidyverse' packages `dplyr` and `tidyr`, as well as plotting with `ggplot2` and `plotly`. In addition, the package provides various utility functions specific to single-cell omics data analysis (e.g., aggregation of cell-level data to pseudobulks).
	"""
	
	homepage = "https://github.com/stemangiola/tidySingleCellExperiment"
	bioc = "tidySingleCellExperiment" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/tidySingleCellExperiment_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/tidySingleCellExperiment/tidySingleCellExperiment_1.12.0.tar.gz"]

	version("1.12.0", sha256="377790b9aad4cfcbd547af705b3fe3db6b79889b9b7c5820470d508652187f23")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ttservice@0.3.8:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-pkgconfig", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-fansi", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
