# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScdha(RPackage):
	"""Single-Cell Decomposition using Hierarchical Autoencoder

	Provides a fast and accurate pipeline for single-cell analyses. 
    The 'scDHA' software package can perform clustering, dimension reduction and visualization, classification, and time-trajectory inference on single-cell data (Tran et.al. (2021) <DOI:10.1038/s41467-021-21312-2>).
	"""
	
	homepage = "https://github.com/duct317/scDHA"
	cran = "scDHA" 

	version("1.2.2", md5="91e67cd0fde98677340d5c3673945a20")
	version("1.2.1", md5="f38bec730454ac153c58f764d06a59d9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcppannoy", type=("build", "run"))
	depends_on("r-torch@0.3:", type=("build", "run"))
	depends_on("r-rhpcblasctl", type=("build", "run"))
	depends_on("r-coro", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
