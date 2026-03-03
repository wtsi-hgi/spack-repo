# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROcf(RPackage):
	"""Ordered Correlation Forest

	Nonparametric estimator for ordered non-numeric outcomes. The estimator modifies a
    standard random forest splitting criterion to build a collection of forests, each estimating the conditional 
    probability of a single class. The package also implements a nonparametric estimator of the covariates’ marginal effects.
	"""
	
	homepage = "https://riccardo-df.github.io/ocf/"
	cran = "ocf" 

	version("1.0.0", md5="7ef3d36a041776cf47ed8d0181b68af8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-orf", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
