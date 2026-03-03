# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmprskqr(RPackage):
	"""Analysis of Competing Risks Using Quantile Regressions

	Estimation, testing and regression modeling of
 subdistribution functions in competing risks using quantile regressions,
 as described in Peng and Fine (2009) <DOI:10.1198/jasa.2009.tm08228>.
	"""
	
	homepage = "https://bitbucket.org/sdlugosz/cmprskqr"
	cran = "cmprskQR" 

	version("0.9.2", md5="3c91a7fa8b65c1853a60c4dd0e8ada68")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
