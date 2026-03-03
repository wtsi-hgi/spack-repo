# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsedfm(RPackage):
	"""Estimate Dynamic Factor Models with Sparse Loadings

	Implementation of various estimation methods for dynamic factor models (DFMs) including principal components analysis (PCA) Stock and Watson (2002) <doi:10.1198/016214502388618960>, 2Stage Giannone et al. (2008) <doi:10.1016/j.jmoneco.2008.05.010>, expectation-maximisation (EM) Banbura and Modugno (2014) <doi:10.1002/jae.2306>, and the novel EM-sparse approach for sparse DFMs Mosley et al. (2023) <arXiv:2303.11892>. Options to use classic multivariate Kalman filter and smoother (KFS) equations from Shumway and Stoffer (1982) <doi:10.1111/j.1467-9892.1982.tb00349.x> or fast univariate KFS equations from Koopman and Durbin (2000) <doi:10.1111/1467-9892.00186>, and options for independent and identically distributed (IID) white noise or auto-regressive (AR(1)) idiosyncratic errors. Algorithms coded in 'C++' and linked to R via 'RcppArmadillo'.   
	"""
	
	cran = "sparseDFM" 

	version("1.0", md5="f17bc069315abde44fa360ed2faf2d5f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
