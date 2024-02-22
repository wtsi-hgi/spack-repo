# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCacimar(RPackage):
	"""Cross-Species Analysis of Cell Identities, Markers and
Regulations

	A toolkit to perform cross-species analysis based on scRNA-seq data. This package contains 5 main features. (1) identify Markers in each cluster. (2) Cell type annotation (3) identify conserved markers. (4) identify conserved cell types. (5) identify conserved modules of regulatory networks.
	"""
	
	homepage = "https://github.com/jiang-junyao/CACIMAR"
	cran = "CACIMAR" 

	version("1.0.0", md5="40510d3f29f7515ec44aa9edb2d9b830")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
