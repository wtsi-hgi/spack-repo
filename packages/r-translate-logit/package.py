# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTranslateLogit(RPackage):
	"""Translation of Logit Regression Coefficients into Percentages

	Translation of logit models coefficients into percentages, following Deauvieau (2010) <doi:10.1177/0759106309352586>.
	"""
	
	cran = "translate.logit" 

	version("1.0", md5="50d5179b967197383f588085a8d4c25f")

	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
