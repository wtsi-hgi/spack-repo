# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPagfl(RPackage):
	"""Joint Estimation and Identification of Latent Groups in Panel
Data Models

	
    In panel data analysis, unobservable group structures are a common challenge. Disregarding group-level heterogeneity by assuming an entirely homogeneous panel can introduce bias. Conversely, estimating individual coefficients for each cross-sectional unit is inefficient and may lead to high uncertainty.
    This package addresses this issue by implementing the pairwise adaptive group fused Lasso (PAGFL) by Mehrabani (2023) <doi:10.1016/j.jeconom.2022.12.002>. 
    PAGFL is an efficient methodology to identify latent group structures and estimate group-specific coefficients simultaneously. 
	"""
	
	homepage = "https://github.com/Paul-Haimerl/PAGFL"
	cran = "PAGFL" 

	version("1.0.1", md5="d2f0625dfb3af7241c829c5fd1aae07b")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
