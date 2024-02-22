# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMme(RPackage):
	"""Multinomial Mixed Effects Models

	Fit Gaussian Multinomial mixed-effects models for small area estimation: Model 1, with one
    random effect in each category of the response variable (Lopez-Vizcaino,E. et al., 2013) <doi:10.1177/1471082X13478873>; Model 2, introducing
    independent time effect; Model 3, introducing correlated time effect.
    mme calculates direct and parametric bootstrap MSE estimators (Lopez-Vizcaino,E et al., 2014) <doi:10.1111/rssa.12085>.
	"""
	
	cran = "mme" 

	version("0.1-6", md5="8b0b2aff8e0b9dcf97b3669e5c74e5e3")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
