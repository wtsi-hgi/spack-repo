# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQrcm(RPackage):
	"""Quantile Regression Coefficients Modeling

	Parametric modeling of quantile regression coefficient functions.
	"""
	
	cran = "qrcm" 

	version("3.1", md5="a88963e132cd48e35bbc89c50973d50e")

	depends_on("r-survival@2.4.1:", type=("build", "run"))
	depends_on("r-pch@2.1:", type=("build", "run"))
	depends_on("r-icenreg@2.0.15:", type=("build", "run"))
