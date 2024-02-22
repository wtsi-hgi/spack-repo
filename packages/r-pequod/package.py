# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPequod(RPackage):
	"""Moderated Regression Package

	Moderated regression with mean and residual centering and simple slopes analysis.
	"""
	
	cran = "pequod" 

	version("0.0-5", md5="f1f5793462de93ee15c6181a00fbca4d")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
