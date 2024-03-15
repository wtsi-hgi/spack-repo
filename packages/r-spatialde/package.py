# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialde(RPackage):
	"""R wrapper for SpatialDE

	SpatialDE is a method to find spatially variable genes (SVG) from spatial transcriptomics data. This package provides wrappers to use the Python SpatialDE library in R, using reticulate and basilisk.
	"""
	
	homepage = "https://github.com/sales-lab/spatialDE"
	bioc = "spatialDE" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/spatialDE_1.8.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/spatialDE/spatialDE_1.8.1.tar.gz"]

	version("1.8.1", md5="8dbe76d7711c00299e180c1c72b056ff")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-basilisk@1.9.10:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
