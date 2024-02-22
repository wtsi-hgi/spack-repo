# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCthresher(RPackage):
	"""Continuous Threshold Expectile Regression

	Estimation and inference methods for the continuous threshold expectile regression.
    It can fit the continuous threshold expectile regression and test the existence of change point,
    for the paper, "Feipeng Zhang and Qunhua Li (2016). A continuous threshold expectile regression, submitted." 
	"""
	
	homepage = "https://arxiv.org/abs/1611.02609"
	cran = "cthreshER" 

	version("1.1.0", md5="4383304fed32a66374698d1229f15db1")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
