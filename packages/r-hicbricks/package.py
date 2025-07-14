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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/HiCBricks_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/HiCBricks/HiCBricks_1.20.0.tar.gz"]

    version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="efffffa51ff278b92110f1d3afe0bd56c34a84bfb44a52a42b2bf0aa398c2015")

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
