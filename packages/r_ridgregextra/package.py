# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRidgregextra(RPackage):
	"""Ridge Regression Parameter Estimation

	It is a package that provides alternative approach for finding optimum parameters of ridge regression. This package focuses on finding the ridge parameter value k which makes the variance inflation factors closest to 1, while keeping them above 1 as addressed by Michael Kutner, Christopher Nachtsheim, John Neter, William Li (2004, ISBN:978-0073108742). Moreover, the package offers end-to-end functionality to find optimum k value and presents the detailed ridge regression results. Finally it shows three sets of graphs consisting k versus variance inflation factors, regression coefficients and standard errors of them. 
	"""
	
	homepage = "https://github.com/filizkrdg/ridgregextra"
	cran = "ridgregextra" 

	version("0.1.1", md5="204b84b3c93610026a7a8e302e96c3fb")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-plotly@4.9:", type=("build", "run"))
	depends_on("r-isdals@3:", type=("build", "run"))
	depends_on("r-mctest@1.3:", type=("build", "run"))
