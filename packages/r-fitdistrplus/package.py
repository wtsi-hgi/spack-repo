# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFitdistrplus(RPackage):
	"""Help to Fit of a Parametric Distribution to Non-Censored or Censored
	Data.

	Extends the fitdistr() function (of the MASS package) with several
	functions to help the fit of a parametric distribution to non-censored or
	censored data. Censored data may contain left censored, right censored and
	interval censored values, with several lower and upper bounds. In addition
	to maximum likelihood estimation (MLE), the package provides moment
	matching (MME), quantile matching (QME) and maximum goodness-of-fit
	estimation (MGE) methods (available only for non-censored data). Weighted
	versions of MLE, MME and QME are available. See e.g. Casella & Berger
	(2002). Statistical inference. Pacific Grove."""

	cran = "fitdistrplus"

	version("1.1-11", md5="512df42bc5b35be4690c17882315f33b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
