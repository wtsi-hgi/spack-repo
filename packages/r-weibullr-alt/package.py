# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeibullrAlt(RPackage):
	"""Accelerated Life Testing Using 'WeibullR'

	Graphical data analysis of accelerated life tests. Methods derived from  Wayne Nelson (1990, ISBN: 9780471522775), William Q. Meeker and  Lois A. Escobar (1998, ISBN: 1-471-14328-6).
	"""
	
	homepage = "http://www.openreliability.org/weibull-r-weibull-analysis-on-r/"
	cran = "WeibullR.ALT" 

	version("0.7.2", md5="e7ff4b475ea50d0f74f9b638d9d572cd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-weibullr", type=("build", "run"))
