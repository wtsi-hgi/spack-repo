# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustlinearreg(RPackage):
	"""Robust Linear Regressions

	Provides an easy way to compute the Theil Sehn Regression method and also the Siegel Regression Method which are both robust methods base on the median of slopes between all pairs of data. In contrast with the least squared linear regression, these methods are not sensitive to outliers. Theil, H. (1992) <doi:10.1007/978-94-011-2546-8_20>, Sen, P. K. (1968) <doi:10.1080/01621459.1968.10480934>.
	"""
	
	cran = "RobustLinearReg" 

	version("1.2.0", md5="4fe10c6d83537ca84c45d210c3f08129")

	depends_on("r@3.1:", type=("build", "run"))
