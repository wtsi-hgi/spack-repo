# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrtreliability(RPackage):
	"""Item Response Theory Reliability

	Estimation of reliability coefficients for ability estimates and sum scores from item response theory models as defined in Cheng, Y., Yuan, K.-H. and Liu, C. (2012) <doi:10.1177/0013164411407315> and Kim, S. and Feldt, L. S. (2010) <doi:10.1007/s12564-009-9062-8>. The package supports the 3-PL and generalized partial credit models and includes estimates of the standard errors of the reliability coefficient estimators, derived in Andersson, B. and Xin, T. (2018) <doi:10.1177/0013164417713570>.
	"""
	
	cran = "irtreliability" 

	version("0.1-1", md5="740a7b2491e6c291d767abde5ede0031")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-ltm", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
	depends_on("r-fastghquad", type=("build", "run"))
