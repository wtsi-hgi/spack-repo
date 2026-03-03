# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBzinb(RPackage):
	"""Bivariate Zero-Inflated Negative Binomial Model Estimator

	Provides a maximum likelihood estimation of Bivariate Zero-Inflated Negative Binomial (BZINB) model or the nested model parameters. Also estimates the underlying correlation of the a pair of count data. See Cho, H., Liu, C., Preisser, J., and Wu, D. (In preparation) for details.
	"""
	
	cran = "bzinb" 

	version("1.0.8", md5="0667f9d89fc72c855a9a78c9c773f894")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
