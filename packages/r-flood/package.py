# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlood(RPackage):
	"""Statistical Methods for the (Regional) Analysis of Flood
Frequency

	Includes several statistical methods for the estimation of parameters and high quantiles of river flow distributions. The focus is on regional estimation based on homogeneity assumptions and computed from multivariate observations (multiple measurement stations).
	For details see Kinsvater et al. (2017) <arXiv:1701.06455>.
	"""
	
	cran = "flood" 

	version("0.1.1", md5="ae5bafc51fc895cf34e4fbacbe95975e")

	depends_on("r-evd", type=("build", "run"))
	depends_on("r-tlmoments", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
