# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2addhaz(RPackage):
	"""R2 Measure of Explained Variation under the Additive Hazards
Model

	R^2 measure of explained variation under the semiparametric additive hazards model is estimated. The measure can be used as a measure of predictive capability and therefore it can be adopted in model selection process. Rava, D. and Xu, R. (2020) <arXiv:2003.09460>.
	"""
	
	cran = "R2Addhaz" 

	version("0.1.0", md5="a879c452058fe4d129e39abfd7aeb443")

	depends_on("r-ahaz", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
