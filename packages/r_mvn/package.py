# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvn(RPackage):
	"""Multivariate Normality Tests

	Performs multivariate normality tests and graphical approaches and
    implements multivariate outlier detection and univariate normality of marginal
    distributions through plots and tests, and performs multivariate Box-Cox transformation 
    (Korkmaz et al, (2014), <https://journal.r-project.org/archive/2014-2/korkmaz-goksuluk-zararsiz.pdf>).
	"""
	
	cran = "MVN" 

	version("5.9", md5="9644d2da276c5450eddbd02caf827baf")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
