# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbmstate(RPackage):
	"""Empirical Bayes Multi-State Cox Model

	Implements an empirical Bayes, multi-state Cox model for survival analysis. Run "?'ebmstate-package'" for details. See also Schall (1991) <doi:10.1093/biomet/78.4.719>.
	"""
	
	cran = "ebmstate" 

	version("0.1.4", md5="15aa19700818381d2fe2665a7a368169")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-survival@2.44.1.1:", type=("build", "run"))
	depends_on("r-mstate@0.2.11:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-hdinterval", type=("build", "run"))
