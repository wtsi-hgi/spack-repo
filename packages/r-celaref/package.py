# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCelaref(RPackage):
	"""Single-cell RNAseq cell cluster labelling by reference

	After the clustering step of a single-cell RNAseq experiment, this package aims to suggest labels/cell types for the clusters, on the basis of similarity to a reference dataset. It requires a table of read counts per cell per gene, and a list of the cells belonging to each of the clusters, (for both test and reference data).
	"""
	
	bioc = "celaref"

	version("1.26.0", commit="eb4248887b574ae8ff915ea30c04c3061980c251")
	version("1.20.0", commit="54fc418c9b1f6c9e8f1b7fa151506282565f6e6a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-mast", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
