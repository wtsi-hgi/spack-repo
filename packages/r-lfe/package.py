# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLfe(RPackage):
	"""Linear Group Fixed Effects.

	Transforms away factors with many levels prior to doing an OLS. Useful for
	estimating linear models with multiple group fixed effects, and for
	estimating linear models which uses factors with many levels as pure
	control variables. See Gaure (2013) <doi:10.1016/j.csda.2013.03.024>
	Includes support for instrumental variables, conditional F statistics for
	weak instruments, robust and multi-way clustered standard errors, as well
	as limited mobility bias correction (Gaure 2014 <doi:10.1002/sta4.68>).
	WARNING: This package is NOT under active development anymore, no further
	improvements are to be expected, and the package is at risk of being
	removed from CRAN."""

	cran = "lfe"

	version("2.9-0", md5="3cd679d5b091c0d9e2673c8f9b16ee6f")

	depends_on("r@2.15.2:", type=("build", "run"))
	depends_on("r-matrix@1.1.2:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
