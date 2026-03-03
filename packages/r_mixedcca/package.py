# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixedcca(RPackage):
	"""Sparse Canonical Correlation Analysis for High-Dimensional Mixed
Data

	Semi-parametric approach for sparse canonical correlation analysis 
    which can handle mixed data types: continuous, binary and truncated continuous.
    Bridge functions are provided to connect Kendall's tau to latent correlation
    under the Gaussian copula model. The methods are described in 
    Yoon, Carroll and Gaynanova (2020) <doi:10.1093/biomet/asaa007> and 
    Yoon, Mueller and Gaynanova (2021) <doi:10.1080/10618600.2021.1882468>.
	"""
	
	cran = "mixedCCA" 

	version("1.6.2", md5="2acc5772774e39d7c8218207659c4602")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-fmultivar", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-latentcor@2.0.1:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
