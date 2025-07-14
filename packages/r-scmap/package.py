# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScmap(RPackage):
	"""A tool for unsupervised projection of single cell RNA-seq data

	Single-cell RNA-seq (scRNA-seq) is widely used to investigate the composition of complex tissues since the technology allows researchers to define cell-types using unsupervised clustering of the transcriptome. However, due to differences in experimental methods and computational analyses, it is often challenging to directly compare the cells identified in two different experiments. scmap is a method for projecting cells from a scRNA-seq experiment on to the cell-types or individual cells identified in a different experiment.
	"""
	
	homepage = "https://github.com/hemberg-lab/scmap"
	bioc = "scmap"

	version("1.30.0", commit="d098bf3898aefd2e693e01562d662acf58595681")
	version("1.24.0", commit="467327ae5079cbddc590807b26111e43e8d445b3")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-googlevis", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
