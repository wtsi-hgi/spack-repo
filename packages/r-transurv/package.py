# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransurv(RPackage):
	"""Transformation Model Based Estimation of Survival and Regression
Under Dependent Truncation and Independent Censoring

	A latent, quasi-independent truncation time is assumed to be linked with the observed dependent truncation time, the event time, and an unknown transformation parameter via a structural transformation model. The transformation parameter is chosen to minimize the conditional Kendall's tau (Martin and Betensky, 2005) <doi:10.1198/016214504000001538> or the regression coefficient estimates (Jones and Crowley, 1992) <doi:10.2307/2336782>. The marginal distribution for the truncation time and the event time are completely left unspecified. The methodology is applied to survival curve estimation and regression analysis.
	"""
	
	homepage = "https://github.com/stc04003/tranSurv"
	cran = "tranSurv" 

	version("1.2.2", md5="2682856b3ce9bcbb1c315abd77523e1e")

	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-truncsp", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-squarem", type=("build", "run"))
