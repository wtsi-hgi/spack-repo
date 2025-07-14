# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHicbricks(RPackage):
	"""Framework for Storing and Accessing Hi-C Data Through HDF Files

	HiCBricks is a library designed for handling large high-resolution Hi-C datasets. Over the years, the Hi-C field has experienced a rapid increase in the size and complexity of datasets. HiCBricks is meant to overcome the challenges related to the analysis of such large datasets within the R environment. HiCBricks offers user-friendly and efficient solutions for handling large high-resolution Hi-C datasets. The package provides an R/Bioconductor framework with the bricks to build more complex data analysis pipelines and algorithms. HiCBricks already incorporates example algorithms for calling domain boundaries and functions for high quality data visualization.
	"""
	
	bioc = "HiCBricks"

	version("1.26.0", commit="773bb6b930a4004ec59795713f410763d3b8171a")
	version("1.20.0", commit="011eda13b66c219cb996898f4798d7b7f47d66d6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
