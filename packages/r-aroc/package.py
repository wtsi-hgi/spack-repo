# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAroc(RPackage):
	"""Covariate-Adjusted Receiver Operating Characteristic Curve
Inference

	Estimates the covariate-adjusted Receiver Operating Characteristic (AROC) curve and pooled (unadjusted) ROC curve by different methods. Inacio de Carvalho, V., and Rodriguez-Alvarez, M. X. (2018) <arXiv:1806.00473>. NOTE: We have created a new package, 'ROCnReg', with more functionalities. It also implements all the methods included in 'AROC'. We, therefore, recommend using 'ROCnReg' ('AROC' will no longer be maintained).
	"""
	
	cran = "AROC" 

	version("1.0-4", md5="b1c602e9e85c4c51bbcd0049a127384d")

	depends_on("r-np", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-nor1mix", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
