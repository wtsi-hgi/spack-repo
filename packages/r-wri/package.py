# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWri(RPackage):
	"""Wasserstein Regression and Inference

	Implementation of the methodologies described in 1) Alexander Petersen, Xi Liu and Afshin A. Divani (2021) <doi:10.1214/20-aos1971>, including global F tests, partial F tests, intrinsic Wasserstein-infinity bands and Wasserstein density bands, and 2) Chao Zhang, Piotr Kokoszka and Alexander Petersen (2022) <doi:10.1111/jtsa.12590>, including estimation, prediction, and inference of the Wasserstein autoregressive models.
	"""
	
	cran = "WRI" 

	version("0.2.0", md5="50d407fa264b6669f0c87c9215f1799e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-fdapace@0.2:", type=("build", "run"))
	depends_on("r-fdadensity@0.1.2:", type=("build", "run"))
	depends_on("r-rfast@1.9.8:", type=("build", "run"))
	depends_on("r-cvxr@0.99.7:", type=("build", "run"))
	depends_on("r-expm@0.999.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-gridextra@2.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-locfit@1.5.9.1:", type=("build", "run"))
	depends_on("r-mvtnorm@1.1.0:", type=("build", "run"))
	depends_on("r-locpol@0.7:", type=("build", "run"))
	depends_on("r-modeest@2.4:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
