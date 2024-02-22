# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REemdsvr(RPackage):
	"""Ensemble Empirical Mode Decomposition and Its Variant Based
Support Vector Regression Model

	Application of Ensemble Empirical Mode Decomposition and its variant based Support Vector regression model for univariate time series forecasting. For method details see Das (2020).<http://krishi.icar.gov.in/jspui/handle/123456789/44138>.
	"""
	
	cran = "EEMDSVR" 

	version("0.1.0", md5="9d2477b7e89c1537f1c00340c3dde5c9")

	depends_on("r-rlibeemd", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
