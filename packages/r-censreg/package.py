# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCensreg(RPackage):
	"""Censored Regression (Tobit) Models

	Maximum Likelihood estimation of censored regression (Tobit) models
   with cross-sectional and panel data.
	"""
	
	homepage = "http://www.sampleSelection.org"
	cran = "censReg" 

	version("0.5-36", md5="988a02d52104bf6085ef9b512f8137e7")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-maxlik@0.7.3:", type=("build", "run"))
	depends_on("r-glmmml@0.81.6:", type=("build", "run"))
	depends_on("r-sandwich@2.2.6:", type=("build", "run"))
	depends_on("r-misctools@0.6.11:", type=("build", "run"))
	depends_on("r-plm", type=("build", "run"))
