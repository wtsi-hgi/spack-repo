# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROssanma(RPackage):
	"""Optimal Sample Size and Allocation with a Network Meta-Analysis

	A system for calculating the minimum total sample size needed to achieve a prespecified power or the optimal allocation for each treatment group with a fixed total sample size to maximize the power.
	"""
	
	homepage = "https://github.com/fangshuye/OssaNMA"
	cran = "OssaNMA" 

	version("0.1.2", md5="362805937278d2e85a9cb77357ad473a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nlcoptim@0.6:", type=("build", "run"))
	depends_on("r-deoptimr@1.0.11:", type=("build", "run"))
