# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLineagepulse(RPackage):
	"""Differential expression analysis and model fitting for single-cell RNA-seq data

	LineagePulse is a differential expression and expression model fitting package tailored to single-cell RNA-seq data (scRNA-seq). LineagePulse accounts for batch effects, drop-out and variable sequencing depth. One can use LineagePulse to perform longitudinal differential expression analysis across pseudotime as a continuous coordinate or between discrete groups of cells (e.g. pre-defined clusters or experimental conditions). Expression model fits can be directly extracted from LineagePulse.
	"""
	
	bioc = "LineagePulse"

	version("1.21.0", sha256="0fd7a5a7620e3da6fd2120a23981545c7bf8ddcb66b22f6f1b0e6b4ff589a127")

	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
