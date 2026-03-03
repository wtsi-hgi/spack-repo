# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMnorm(RPackage):
	"""Multivariate Normal Distribution

	Calculates and differentiates probabilities and density of (conditional) multivariate normal distribution and Gaussian copula (with various marginal distributions) using methods described in A. Genz (2004) <doi:10.1023/B:STCO.0000035304.20635.31>, A. Genz, F. Bretz (2009) <doi:10.1007/978-3-642-01689-9>, H. I. Gassmann (2003) <doi:10.1198/1061860032283> and E. Kossova, B. Potanin (2018) <https://ideas.repec.org/a/ris/apltrx/0346.html>.
	"""
	
	cran = "mnorm" 

	version("1.2.2", md5="38995531305aea52985dbd4b620a081e")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-hpa", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
