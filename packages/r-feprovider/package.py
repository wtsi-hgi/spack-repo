# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFeprovider(RPackage):
	"""Fixed Effects Logistic Model with High-Dimensional Parameters

	A structured profile likelihood algorithm for the logistic fixed effects model and an approximate expectation maximization (EM) algorithm for the logistic mixed effects model. Based on He, K., Kalbfleisch, J.D., Li, Y. and Li, Y. (2013) <doi:10.1007/s10985-013-9264-6>.
	"""
	
	cran = "FEprovideR" 

	version("1.1", md5="c2d0e8c1709ca1b884c71e4e412dea9b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-poibin", type=("build", "run"))
