# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamm(RPackage):
	"""Some Algorithms for Mixed Models

	This program can be used to fit Gaussian linear mixed models (LMM). Univariate and multivariate response models, multiple variance components, as well as, certain correlation and covariance structures are supported. In many occasions, the user can pick one of the several mixed model fitting algorithms, which are explained further in the details section. Some algorithms are specific to certain types of models (univariate or multivariate, diagonal or non-diagonal residual, one or multiple variance components, etc,...).
	"""
	
	cran = "SAMM" 

	version("1.1.1", md5="a4809fd2a9e46f3cc0a79dc223bf5619")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
