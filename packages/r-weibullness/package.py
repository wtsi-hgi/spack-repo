# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeibullness(RPackage):
	"""Goodness-of-Fit Test for Weibull Distribution (Weibullness)

	Conducts a goodness-of-fit test for the Weibull distribution (referred to as the weibullness test) and furnishes parameter estimations for both the two-parameter and three-parameter Weibull distributions. Notably, the threshold parameter is derived through correlation from the Weibull plot. Additionally, this package conducts goodness-of-fit assessments for the exponential, Gumbel, and inverse Weibull distributions, accompanied by parameter estimations.
  For more details, see Park (2017) <doi:10.23055/ijietap.2017.24.4.2848>, 
  Park (2018) <doi:10.1155/2018/6056975>, and Park (2023) <doi:10.3390/math11143156>. 
  This work was supported by the National Research Foundation of Korea (NRF) grants funded by 
  the Korea government (MSIT) (No. 2022R1A2C1091319, RS-2023-00242528).
	"""
	
	homepage = "https://AppliedStat.GitHub.io/R/"
	cran = "weibullness" 

	version("1.24.1", md5="3725675d4d305d1ffe3f7ca8d2392132")

	depends_on("r@4:", type=("build", "run"))
