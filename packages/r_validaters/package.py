# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RValidaters(RPackage):
	"""One-Sided Multivariate Testing Procedures for Rating Systems

	An implementation of statistical tests for the validation of rating systems as described in the ECB Working paper ''Advances in multivariate back-testing for credit risk underestimation'', by F. Coppens, M. Mayer, L. Millischer, F.  Resch, S. Sauer, K. Schulze (ECB WP series, forthcoming).
	"""
	
	cran = "validateRS" 

	version("1.0.0", md5="81e8d628074ac0a7ca4ad855bd6b1b1e")

	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-triangle", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
