# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinypredict(RPackage):
	"""Predictions using Shiny

	Creates 'shiny' application ('app.R') for making predictions based on lm(), glm(), or coxph() models.
	"""
	
	cran = "shinyPredict" 

	version("0.1.1", md5="51b473f4d19786171b0dd7ba5a865e30")

	depends_on("r@3.6:", type=("build", "run"))
