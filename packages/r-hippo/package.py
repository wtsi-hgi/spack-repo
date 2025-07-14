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

	version("1.20.0", commit="fba8a0a800f177a6d8501d56f251b37f95fbd6c3")
	version("1.14.0", commit="7d5a5b234b9f888393cf84afc5963e5f9bf2f379")

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
