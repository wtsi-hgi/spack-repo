# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRelaimpo(RPackage):
	"""Relative Importance of Regressors in Linear Models

	Provides several metrics for assessing relative importance in linear models. These can be printed, plotted and bootstrapped. The recommended metric is lmg, which provides a decomposition of the model explained variance into non-negative contributions. There is a version of this package available that additionally provides a new and also recommended metric called pmvd. If you are a non-US user, you can download this extended version from Ulrike Groempings web site.
	"""
	
	homepage = "https://prof.bht-berlin.de/groemping/relaimpo/"
	cran = "relaimpo" 

	version("2.2-7", md5="c1f96be099591ec9486c167dd47e2dfe")

	depends_on("r@2.2.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-mitools", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
