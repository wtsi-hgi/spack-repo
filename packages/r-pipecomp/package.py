# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPipecomp(RPackage):
	"""pipeComp pipeline benchmarking framework

	A simple framework to facilitate the comparison of pipelines involving various steps and parameters. The `pipelineDefinition` class represents pipelines as, minimally, a set of functions consecutively executed on the output of the previous one, and optionally accompanied by step-wise evaluation and aggregation functions. Given such an object, a set of alternative parameters/methods, and benchmark datasets, the `runPipeline` function then proceeds through all combinations arguments, avoiding recomputing the same step twice and compiling evaluations on the fly to avoid storing potentially large intermediate data.
	"""
	
	homepage = "https://doi.org/10.1186/s13059-020-02136-7"
	bioc = "pipeComp"

	version("1.18.0", commit="151589a454e199a31a5cacabaa9c3804ac50a835")
	version("1.12.0", commit="b567066af753cfdee122178bc822bf0af9f68b82")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-aricode", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-scran", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-randomcolor", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-intrinsicdimension", type=("build", "run"))
	depends_on("r-scater", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
