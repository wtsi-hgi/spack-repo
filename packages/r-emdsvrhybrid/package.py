# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmdsvrhybrid(RPackage):
	"""Empirical Mode Decomposition Based Support Vector Regression
Model

	Description: Application of empirical mode decomposition based support vector regression model for nonlinear and non stationary univariate time series forecasting. For method details see (i) Choudhury (2019) <http://krishi.icar.gov.in/jspui/handle/123456789/44873>; (ii) Das (2020) <http://krishi.icar.gov.in/jspui/handle/123456789/43174>; (iii) Das (2023) <http://krishi.icar.gov.in/jspui/handle/123456789/77772>.
	"""
	
	cran = "EMDSVRhybrid" 

	version("0.2.0", md5="896c713a311808a8983f4ffdfd01af8d")

	depends_on("r-emd", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
