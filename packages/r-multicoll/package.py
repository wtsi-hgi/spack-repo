# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMulticoll(RPackage):
	"""Collinearity Detection in a Multiple Linear Regression Model

	The detection of worrying approximate collinearity in a multiple linear regression model is a problem addressed in all existing statistical packages. However, we have detected deficits regarding to the incorrect treatment of qualitative independent variables and the role of the intercept of the model. The objective of this package is to correct these deficits. In this package will be available detection and treatment techniques traditionally used as the recently developed.
	"""
	
	homepage = "http://colldetreat.r-forge.r-project.org/"
	cran = "multiColl" 

	version("2.0", md5="71e021a21608ae598152da4e6d5de2d9")

	depends_on("r@3.5:", type=("build", "run"))
