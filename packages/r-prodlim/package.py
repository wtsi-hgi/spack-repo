# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProdlim(RPackage):
	"""Product-Limit Estimation for Censored Event History Analysis.

	Product-Limit Estimation for Censored Event History Analysis. Fast and user
	friendly implementation of nonparametric estimators for censored event
	history (survival) analysis. Kaplan-Meier and Aalen-Johansen method."""

	cran = "prodlim"

	version("2023.08.28", md5="659174e40f0c8061d3312aa09464a838")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-diagram", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-lava", type=("build", "run"))
