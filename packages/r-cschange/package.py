# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCschange(RPackage):
	"""Testing for Change in C-Statistic

	Calculate the confidence interval and p value for change in C-statistic. The adjusted C-statistic is calculated by using formula as "Somers' Dxy rank correlation"/2+0.5. The confidence interval was calculated by using the bootstrap method. The p value was calculated by using the Z testing method. Please refer to the article of Peter Ganz et al. (2016) <doi:10.1001/jama.2016.5951>.
	"""
	
	cran = "CsChange" 

	version("0.1.7", md5="8882ed82a6d722c8676ef508334e1061")

	depends_on("r-rms", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
