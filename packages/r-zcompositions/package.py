# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZcompositions(RPackage):
	"""Treatment of Zeros, Left-Censored and Missing Values in Compositional
	Data Sets.

	Principled methods for the imputation of zeros, left-censored and missing
	data in compositional data sets (Palarea-Albaladejo and Martin-Fernandez
	(2015) <doi:10.1016/j.chemolab.2015.02.019>)."""

	cran = "zCompositions"

	version("1.5.0-1", md5="d4491a01b81a2e44514e1b32c4ee736f")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nada", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
