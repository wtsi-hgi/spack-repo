# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REplsim(RPackage):
	"""Partial Linear Single Index Models for Environmental Mixture
Analysis

	Collection of ancillary functions and utilities for Partial Linear Single Index Models for Environmental mixture analyses, which currently provides functions for scalar outcomes. The outputs of these functions include the single index function, single index coefficients, partial linear coefficients, mixture overall effect, exposure main and interaction effects, and differences of quartile effects. In the future, we will add functions for binary, ordinal, Poisson, survival, and longitudinal outcomes, as well as models for time-dependent exposures. See Wang et al (2020) <doi:10.1186/s12940-020-00644-4> for an overview. 
	"""
	
	homepage = "https://github.com/YuyanWangSixTwo/EPLSIM"
	cran = "EPLSIM" 

	version("0.1.0", md5="3f01b16c0af89bbbee5c5a0bf86afd2c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-citools", type=("build", "run"))
