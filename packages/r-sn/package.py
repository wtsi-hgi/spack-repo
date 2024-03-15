# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSn(RPackage):
	"""The Skew-Normal and Related Distributions Such as the Skew-t.

	Build and manipulate probability distributions of the skew-normal family
	and some related ones, notably the skew-t family, and provide related
	statistical methods for data fitting and diagnostics, in the univariate and
	the multivariate case."""

	cran = "sn"

	license("GPL-2.0-only OR GPL-3.0-only")

	version("2.1.1", md5="f77c36f37cd65ecfedde2e34f7caa44a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mnormt@2:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
