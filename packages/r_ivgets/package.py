# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIvgets(RPackage):
	"""General to Specific Modeling and Indicator Saturation in 2SLS
Models

	Provides facilities of general to specific model selection for
    exogenous regressors in 2SLS models. Furthermore, indicator saturation
    methods can be used to detect outliers and structural breaks in the sample.
	"""
	
	homepage = "https://github.com/jkurle/ivgets"
	cran = "ivgets" 

	version("0.1.1", md5="873c67074e7756e5df2360fff0405f8e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gets@0.36:", type=("build", "run"))
	depends_on("r-ivreg", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
