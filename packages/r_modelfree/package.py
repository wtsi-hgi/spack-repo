# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModelfree(RPackage):
	"""Model-Free Estimation of a Psychometric Function

	Local linear estimation of psychometric functions. Provides functions for nonparametric estimation of a psychometric function and for estimation of a derived threshold and slope, and their standard deviations and confidence intervals.
	"""
	
	homepage = "www.R-project.org"
	cran = "modelfree" 

	version("1.2", md5="cb6dccdefa858a2aef5c8094822f97ad")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-polynomf", type=("build", "run"))
