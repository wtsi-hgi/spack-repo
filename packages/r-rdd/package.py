# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdd(RPackage):
	"""Regression Discontinuity Estimation

	Provides the tools to undertake estimation in
    Regression Discontinuity Designs. Both sharp and fuzzy designs are
    supported. Estimation is accomplished using local linear regression.
    A provided function will utilize Imbens-Kalyanaraman optimal
    bandwidth calculation. A function is also included to test the
    assumption of no-sorting effects.
	"""
	
	cran = "rdd" 

	version("0.57", md5="2572a1e5e773dbd0efe3a8b86ab2c261")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-aer", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
