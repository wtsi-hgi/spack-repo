# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBbssl(RPackage):
	"""Bayesian Bootstrap Spike-and-Slab LASSO

	Posterior sampling for Spike-and-Slab LASSO prior in linear models from Nie and Rockova <arXiv:2011.14279>.
	"""
	
	cran = "BBSSL" 

	version("0.1.0", md5="da7ddbf902e9bc2674470fae0b4d2948")

	depends_on("r-svmisc@1.1:", type=("build", "run"))
	depends_on("r-mvnfast@0.2.5:", type=("build", "run"))
	depends_on("r-rmutil@1.1.3:", type=("build", "run"))
	depends_on("r-greybox@0.5.1:", type=("build", "run"))
	depends_on("r-statmod@1.4.30:", type=("build", "run"))
	depends_on("r-matrix@1.2.17:", type=("build", "run"))
	depends_on("r-glmnet@2.0.16:", type=("build", "run"))
	depends_on("r-truncnorm@1.0.8:", type=("build", "run"))
