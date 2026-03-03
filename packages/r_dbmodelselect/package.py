# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbmodelselect(RPackage):
	"""Distribution-Based Model Selection

	Perform model selection using distribution and probability-based methods,
	including standardized AIC, BIC, and AICc. These standardized information criteria
	allow one to perform model selection in a way similar to the prevalent "Rule of 2"
	method, but formalize the method to rely on probability theory. A novel goodness-of-fit
	procedure for assessing linear regression models is also available. This test relies on
	theoretical properties of the estimated error variance for a normal linear regression
	model, and employs a bootstrap procedure to assess the null hypothesis that the fitted
	model shows no lack of fit. For more information, see Koeneman and Cavanaugh (2023)
	<arXiv:2309.10614>. Functionality to perform all subsets linear or generalized linear
	regression is also available.
	"""
	
	homepage = "https://github.com/shkoeneman/DBModelSelect"
	cran = "DBModelSelect" 

	version("0.2.0", md5="ad78eec346e15131a0380e24e98e6b8a")

	depends_on("r@4.1:", type=("build", "run"))
