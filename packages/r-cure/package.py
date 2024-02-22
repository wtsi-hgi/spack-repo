# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCure(RPackage):
	"""Parametric Cure Model Estimation

	Contains functions for estimating generalized parametric mixture and non-mixture cure models <doi:10.1016/j.cmpb.2022.107125>, loss of lifetime, mean residual lifetime, and crude event probabilities.
	"""
	
	homepage = "https://github.com/LasseHjort/cuRe"
	cran = "cuRe" 

	version("1.1.1", md5="4d5853263105e4485d536ee6f6a4a0c0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rstpm2", type=("build", "run"))
	depends_on("r-date", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-relsurv", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
