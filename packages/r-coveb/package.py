# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoveb(RPackage):
	"""Empirical Bayes estimate of block diagonal covariance matrices

	Using bayesian methods to estimate correlation matrices assuming that they can be written and estimated as block diagonal matrices. These block diagonal matrices are determined using shrinkage parameters that values below this parameter to zero.
	"""
	
	bioc = "covEB" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/covEB_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/covEB/covEB_1.28.0.tar.gz"]

    version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="d3f16a0d1b4ff63d493e1a82b5a53419d9feb28bd983a1f4ff1ae3b6fa800428")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
