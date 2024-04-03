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
	version("1.1-8", sha256="f3c72310f40773b3839a9506c3cb781d044e09b94f2f38d332bb24e5f9960f5a")
	version("1.1-6", sha256="17c2990041a3bb7479f3c3a6d13d96c989db8eaddab17eff7e1fbe172a5b96be")
	version("1.1-3", sha256="776d5456e14398e44b78b3d7db526559bb7a3537e546a29c88aa192141c756de")
	version("1.0-14", sha256="85082590f62aa08d99048ea3414c5cc1e5b780d97b3779d2397c6cb435470083")
	version("1.1-11", md5="512df42bc5b35be4690c17882315f33b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
