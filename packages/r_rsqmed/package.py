# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsqmed(RPackage):
	"""Total Mediation Effect Size Measure for High-Dimensional
Mediators

	An implementation of calculating the R-squared measure as a total mediation effect size measure and its confidence interval for moderate- or high-dimensional mediator models. It gives an option to filter out non-mediators using variable selection methods. The original R package is directly related to the paper Yang et al (2021) "Estimation of mediation effect for high-dimensional omics mediators with application to the Framingham Heart Study" <doi:10.1101/774877>. The new version contains a choice of using cross-fitting, which is computationally faster. The details of the cross-fitting method are available in the paper Xu et al (2023) "Speeding up interval estimation for R2-based mediation effect of high-dimensional mediators via cross-fitting" <doi:10.1101/2023.02.06.527391>.
	"""
	
	cran = "RsqMed" 

	version("1.1", md5="cf1df8d4184ceb63959fd6a3e4f603c3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sis@0.8:", type=("build", "run"))
	depends_on("r-gmmat@1.4.1:", type=("build", "run"))
