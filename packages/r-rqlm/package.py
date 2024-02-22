# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRqlm(RPackage):
	"""Modified Poisson and Least-Squares Regressions for Binary
Outcome

	Modified Poisson and least-squares regression analyses for binary outcomes of Zou (2004) <doi:10.1093/aje/kwh090> and Cheung (2007) <doi:10.1093/aje/kwm223> have been standard multivariate analysis methods to estimate risk ratio and risk difference in clinical and epidemiological studies. This R package involves an easy-to-handle function to implement these analyses by simple commands. Also, recent studies have shown the ordinary robust variance estimator possibly has serious bias under small or moderate sample size situations for these methods. This package also provides computational tools to calculate alternative accurate confidence intervals (Noma and Gosho (2024) <Forthcoming>).
	"""
	
	cran = "rqlm" 

	version("1.2-1", md5="3b4afb8e4bba545971e0b0aae8d20855")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
