# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlockcv(RPackage):
	"""Spatial and Environmental Blocking for K-Fold and LOO
Cross-Validation

	Creating spatially or environmentally separated folds for cross-validation to provide a robust error estimation in spatially structured environments; Investigating and visualising the effective range of spatial autocorrelation in continuous raster covariates and point samples to find an initial realistic distance band to separate training and testing datasets spatially described in Valavi, R. et al. (2019) <doi:10.1111/2041-210X.13107>.
	"""
	
	homepage = "https://github.com/rvalavi/blockCV"
	cran = "blockCV" 

	version("3.1-3", md5="1b14f4de3d5ca965cdc7ed44173baeb2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf@1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
