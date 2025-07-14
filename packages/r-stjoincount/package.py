# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStjoincount(RPackage):
	"""stJoincount - Join count statistic for quantifying spatial correlation between clusters

	stJoincount facilitates the application of join count analysis to spatial transcriptomic data generated from the 10x Genomics Visium platform. This tool first converts a labeled spatial tissue map into a raster object, in which each spatial feature is represented by a pixel coded by label assignment. This process includes automatic calculation of optimal raster resolution and extent for the sample. A neighbors list is then created from the rasterized sample, in which adjacent and diagonal neighbors for each pixel are identified. After adding binary spatial weights to the neighbors list, a multi-categorical join count analysis is performed to tabulate "joins" between all possible combinations of label pairs. The function returns the observed join counts, the expected count under conditions of spatial randomness, and the variance calculated under non-free sampling. The z-score is then calculated as the difference between observed and expected counts, divided by the square root of the variance.
	"""
	
	homepage = "https://github.com/Nina-Song/stJoincount"
	bioc = "stJoincount" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/stJoincount_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/stJoincount/stJoincount_1.4.0.tar.gz"]

    version("1.10.0", tag="RELEASE_3_21")
	version("1.4.0", sha256="9f29095aaf05ac1d2f4bd293ef0e415a947ed4d6f88190c589ca2ea43aaec747")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
