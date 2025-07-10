# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGranulator(RPackage):
	"""Rapid benchmarking of methods for *in silico* deconvolution of bulk RNA-seq data

	granulator is an R package for the cell type deconvolution of heterogeneous tissues based on bulk RNA-seq data or single cell RNA-seq expression profiles. The package provides a unified testing interface to rapidly run and benchmark multiple state-of-the-art deconvolution methods. Data for the deconvolution of peripheral blood mononuclear cells (PBMCs) into individual immune cell types is provided as well.
	"""
	
	homepage = "https://github.com/xanibas/granulator"
	bioc = "granulator" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/granulator_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/granulator/granulator_1.10.0.tar.gz"]

	version("1.10.0", sha256="01226099d1d2a13013135583a03f3b12ec2f5b5eeacd541e70c3ab8e75c9686b")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-epir", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dtangle", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggplotify", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
