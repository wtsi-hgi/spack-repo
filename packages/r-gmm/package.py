# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmm(RPackage):
	"""Generalized Method of Moments and Generalized Empirical
Likelihood

	It is a complete suite to estimate models based on moment conditions. It includes the two step Generalized method of moments (Hansen 1982; <doi:10.2307/1912775>), the iterated GMM and continuous updated estimator (Hansen, Eaton and Yaron 1996; <doi:10.2307/1392442>) and several methods that belong to the Generalized Empirical Likelihood family of estimators (Smith 1997; <doi:10.1111/j.0013-0133.1997.174.x>, Kitamura 1997; <doi:10.1214/aos/1069362388>, Newey and Smith 2004; <doi:10.1111/j.1468-0262.2004.00482.x>, and Anatolyev 2005 <doi:10.1111/j.1468-0262.2005.00601.x>).	
	"""
	
	cran = "gmm" 

	version("1.8", md5="179ff6fd654a5cc63f46c9e6be9e905a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
