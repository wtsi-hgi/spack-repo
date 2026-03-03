# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFenmlm(RPackage):
	"""Fixed Effects Nonlinear Maximum Likelihood Models

	Efficient estimation of maximum likelihood models with multiple fixed-effects. Standard-errors can easily and flexibly be clustered and estimations exported.
	"""
	
	cran = "FENmlm" 

	version("2.4.4", md5="52b85b9f8880382788bba29c5be189f1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
