# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeibullr(RPackage):
	"""Weibull Analysis for Reliability Engineering

	Life data analysis in the graphical tradition of Waloddi Weibull. Methods derived from Robert B. Abernethy (2008, ISBN 0-965306-3-2), Wayne Nelson (1982, ISBN: 9780471094586), William Q. Meeker and  Lois A. Escobar (1998, ISBN: 1-471-14328-6), John I. McCool, (2012, ISBN: 9781118217986).
	"""
	
	homepage = "http://www.openreliability.org/weibull-r-weibull-analysis-on-r/"
	cran = "WeibullR" 

	version("1.2.1", md5="310e4aa698caadaadc2fd291c60c3db5")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
