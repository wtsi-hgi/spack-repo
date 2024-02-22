# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbreaks(RPackage):
	"""Estimation and Inference for Structural Breaks in Linear
Regression Models

	Functions provide comprehensive treatments for estimating, inferring, testing and model selecting in linear regression models with structural breaks. The tests, estimation methods, inference and information criteria implemented are discussed in Bai and Perron (1998) "Estimating and Testing Linear Models with Multiple Structural Changes" <doi:10.2307/2998540>.
	"""
	
	homepage = "https://github.com/RoDivinity/mbreaks"
	cran = "mbreaks" 

	version("1.0.0", md5="b22030d92af01bdfe404b9593608de7f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
