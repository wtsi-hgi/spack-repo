# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixlm(RPackage):
	"""Mixed Model ANOVA and Statistics for Education

	The main functions perform mixed models analysis by least squares
    or REML by adding the function r() to formulas of lm() and glm(). A collection of
    text-book statistics for higher education is also included, e.g. modifications
    of the functions lm(), glm() and associated summaries from the package 'stats'.
	"""
	
	homepage = "https://github.com/khliland/mixlm/"
	cran = "mixlm" 

	version("1.3.0", md5="cf7e78809d1755e6014014b9fda04cf5")

	depends_on("r-car", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
