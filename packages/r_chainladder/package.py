# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChainladder(RPackage):
	"""Statistical Methods and Models for Claims Reserving in General
Insurance

	Various statistical methods and models which are
    typically used for the estimation of outstanding claims reserves
    in general insurance, including those to estimate the claims
    development result as required under Solvency II.
	"""
	
	homepage = "https://mages.github.io/ChainLadder/"
	cran = "ChainLadder" 

	version("0.2.18", md5="42fea47dd6ebda648d9f977760ca0746")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-actuar", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-tweedie", type=("build", "run"))
	depends_on("r-systemfit", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-cplm@0.7.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
