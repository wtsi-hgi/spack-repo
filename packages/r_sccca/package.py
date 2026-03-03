# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSccca(RPackage):
	"""Single-Cell Correlation Based Cell Type Annotation

	Performing cell type annotation based on cell markers from a unified database. The approach utilizes correlation-based approach combined with association analysis using Fisher-exact and phyper statistical tests (Upton, Graham JG. (1992) <DOI:10.2307/2982890>).
	"""
	
	cran = "sccca" 

	version("0.1.1", md5="e80cb6334069228af7420514831ff860")

	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-hgnchelper", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
