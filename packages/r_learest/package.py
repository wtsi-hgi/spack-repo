# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLearest(RPackage):
	"""Border and Area Estimation of Data Measured with Additive Error

	Provides methods for estimating borders of uniform distribution on
  the interval (one-dimensional) and on the elliptical domain (two-dimensional)
  under measurement errors. For one-dimensional case, it also estimates the
  length of underlying uniform domain and tests the hypothesized length against
  two-sided or one-sided alternatives. For two-dimensional case, it estimates
  the area of underlying uniform domain. It works with numerical inputs as well
  as with pictures in JPG format.
	"""
	
	cran = "LeArEst" 

	version("1.0.0", md5="7ed3fa083b5e06bbadd64af972d1690f")

	depends_on("r-conicfit", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-opencpu@2:", type=("build", "run"))
