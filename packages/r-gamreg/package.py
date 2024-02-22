# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamreg(RPackage):
	"""Robust and Sparse Regression via Gamma-Divergence

	Robust regression via gamma-divergence with L1, elastic net and ridge.
	"""
	
	cran = "gamreg" 

	version("0.3", md5="e8cb5431eb7d8c4d8b0c2d148214e9e0")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-robusthd", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
