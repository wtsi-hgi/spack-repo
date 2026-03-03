# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwrr(RPackage):
	"""Fits Geographically Weighted Regression Models with Diagnostic
Tools

	Fits geographically weighted regression (GWR) models and has tools to diagnose and remediate collinearity in the GWR models. Also fits geographically weighted ridge regression (GWRR) and geographically weighted lasso (GWL) models. See Wheeler (2009) <doi:10.1068/a40256> and Wheeler (2007) <doi:10.1068/a38325> for more details.
	"""
	
	cran = "gwrr" 

	version("0.2-2", md5="862087f0969596dcf5510ad03998290e")

	depends_on("r-fields", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
