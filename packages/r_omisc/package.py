# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmisc(RPackage):
	"""Univariate Bootstrapping and Other Things

	Primarily devoted to implementing the Univariate Bootstrap (as well as the Traditional Bootstrap). In addition there are multiple functions for DeFries-Fulker behavioral genetics models. The univariate bootstrapping functions, DeFries-Fulker functions, regression and traditional bootstrapping functions form the original core. Additional features may come online later, however this software is a work in progress. For more information about univariate bootstrapping see: Lee and Rodgers (1998) and Beasley et al (2007) <doi:10.1037/1082-989X.12.4.414>.
	"""
	
	cran = "Omisc" 

	version("0.1.5", md5="ec3620cb09faa7616def12c3c482cd7c")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
