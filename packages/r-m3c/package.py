# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RM3c(RPackage):
	"""Monte Carlo Reference-based Consensus Clustering

	M3C is a consensus clustering algorithm that uses a Monte Carlo simulation to eliminate overestimation of K and can reject the null hypothesis K=1.
	"""
	
	bioc = "M3C" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/M3C_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/M3C/M3C_1.24.0.tar.gz"]

	version("1.24.0", md5="e04534528d39712026e9b1de15a12c3d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
