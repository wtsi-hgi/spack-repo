# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHippo(RPackage):
	"""Heterogeneity-Induced Pre-Processing tOol

	For scRNA-seq data, it selects features and clusters the cells simultaneously for single-cell UMI data. It has a novel feature selection method using the zero inflation instead of gene variance, and computationally faster than other existing methods since it only relies on PCA+Kmeans rather than graph-clustering or consensus clustering.
	"""
	
	homepage = "https://github.com/tk382/HIPPO"
	bioc = "HIPPO" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/HIPPO_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/HIPPO/HIPPO_1.14.0.tar.gz"]

	version("1.14.0", md5="6c249e5f8b3f2a0622642c945e8d0566")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
