# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPerryexamples(RPackage):
	"""Examples for Integrating Prediction Error Estimation into
Regression Models

	Examples for integrating package 'perry' for prediction error estimation into regression models.
	"""
	
	cran = "perryExamples" 

	version("0.1.1", md5="5f0f9c3e87b21dd82dc477e3ff9fce76")

	depends_on("r@2.14.1:", type=("build", "run"))
	depends_on("r-perry@0.3:", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
