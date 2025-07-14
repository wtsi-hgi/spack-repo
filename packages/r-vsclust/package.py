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

	version("1.10.0", tag="RELEASE_3_21")
	version("1.4.0", sha256="3438992407e27098a9304721bbb07d30fb85d3c238bdda0d96a5cca9d0e9748d")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
