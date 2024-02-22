# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmcm(RPackage):
	"""Fast Estimation of Gaussian Mixture Copula Models

	Unsupervised Clustering and Meta-analysis using Gaussian Mixture
    Copula Models.
	"""
	
	homepage = "https://github.com/AEBilgrau/GMCM"
	cran = "GMCM" 

	version("1.4", md5="6f090f3ab2e32dcde356f3473f0b3402")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
