# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGfdrmst(RPackage):
	"""Multiple RMST-Based Tests in General Factorial Designs

	We implemented multiple tests based on the restricted mean survival time (RMST) for general factorial designs as described in Munko et al. (2024) <doi:10.1002/sim.10017>. Therefore, an asymptotic test, a groupwise bootstrap test, and a permutation test are incorporated with a Wald-type test statistic. The asymptotic and groupwise bootstrap test take the asymptotic exact dependence structure of the test statistics into account to gain more power. Furthermore, confidence intervals for RMST contrasts can be calculated and plotted and a stepwise extension that can improve the power of the multiple tests is available.
	"""
	
	cran = "GFDrmst" 

	version("0.1.0", md5="f0111a2976df4bbf7feedeabbc359081")

	depends_on("r-gfdmcv", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinymatrix", type=("build", "run"))
	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-tippy@0.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mass@7.3.53:", type=("build", "run"))
	depends_on("r-plyr@1.8.6:", type=("build", "run"))
	depends_on("r-shinyjs@2:", type=("build", "run"))
	depends_on("r-shinythemes@1.1.2:", type=("build", "run"))
