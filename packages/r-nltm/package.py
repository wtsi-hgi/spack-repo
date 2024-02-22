# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNltm(RPackage):
	"""Non-Linear Transformation Models

	Fits a non-linear transformation model ('nltm') for
        analyzing survival data, see Tsodikov (2003) <doi:10.1111/1467-9868.00414>. The
        class of 'nltm' includes the following currently supported
        models: Cox proportional hazard, proportional hazard cure,
        proportional odds, proportional hazard - proportional hazard
        cure, proportional hazard - proportional odds cure, Gamma
        frailty, and proportional hazard - proportional odds.
	"""
	
	homepage = "https://github.com/mclements/nltm"
	cran = "nltm" 

	version("1.4.5", md5="e3eff7fd2287be345e564595ea3a5cc5")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r@2.8.1:", type=("build", "run"))
