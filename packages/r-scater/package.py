# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScater(RPackage):
	"""Single-Cell Analysis Toolkit for Gene Expression Data in R.

	A collection of tools for doing various analyses of single-cell RNA-seq
	gene expression data, with a focus on quality control and
	visualization."""

	bioc = "scater"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/scater_1.30.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/scater/scater_1.30.1.tar.gz"]

	version("1.30.1", md5="c161043392323318c01792e2de828ad5")

	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-scuttle", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
	depends_on("r-beachmat", type=("build", "run"))
	depends_on("r-biocneighbors", type=("build", "run"))
	depends_on("r-biocsingular", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggbeeswarm", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcppml", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggrastr", type=("build", "run"))
