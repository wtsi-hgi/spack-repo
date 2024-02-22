# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCenbar(RPackage):
	"""Broken Adaptive Ridge AFT Model with Censored Data

	Broken adaptive ridge estimator for censored data is used to
  select variables and estimate their coefficients in the semi-parametric 
  accelerated failure time model for right-censored survival data.
	"""
	
	cran = "CenBAR" 

	version("0.1.1", md5="f52df648e067ee49152e4076c4de7301")

	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-cvtools", type=("build", "run"))
