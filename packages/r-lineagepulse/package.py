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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/LineagePulse_1.21.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/LineagePulse/LineagePulse_1.21.0.tar.gz"]

	version("1.21.0", md5="c17825342234d6f0e327853b8fc52944")

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
