# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCenscov(RPackage):
	"""Linear Regression with a Randomly Censored Covariate

	Implementations of threshold regression approaches for linear
	     regression models with a covariate subject to random censoring,
	     including deletion threshold regression and completion threshold regression.
	     Reverse survival regression, which flip the role of response variable and the
	     covariate, is also considered.
	"""
	
	cran = "censCov" 

	version("1.0-0", md5="8ea8b5ac92e3038358758625e999d545")

	depends_on("r-survival", type=("build", "run"))
