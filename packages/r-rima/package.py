# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRima(RPackage):
	"""RIMA (RIgorous Matching of single-cell transcriptomics Atlases) is an R package for matching single-cell transcriptomics data across two datasets at the level of cell neighbourhoods. It is particularly useful in scenarios where data integration is difficult, such as cross-species analyses, or comparisons across different experimental conditions."""
	
	homepage = "https://github.com/ma-jacques/RIMA"
	git = "https://github.com/ma-jacques/RIMA.git"

	version("2026-02-17", commit="b0aacbdc24ec98c3cc989a98229f6a3d70fc1d19")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-milor", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-rdist", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
