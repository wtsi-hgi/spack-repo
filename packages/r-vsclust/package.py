# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVsclust(RPackage):
	"""Feature-based variance-sensitive quantitative clustering

	Feature-based variance-sensitive clustering of omics data. Optimizes cluster assignment by taking into account individual feature variance. Includes several modules for statistical testing, clustering and enrichment analysis.
	"""
	
	bioc = "vsclust" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/vsclust_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/vsclust/vsclust_1.4.0.tar.gz"]

	version("1.4.0", md5="0c492a6d65d0b230211a0f95706b51a4")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
