# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredreliability(RPackage):
	"""Estimates Reliability of Individual Supervised Learning
Predictions

	An implementation of reliability estimation methods described in the paper (Bosnic, Z., & Kononenko, I. (2008) <doi:10.1007/s10489-007-0084-9>), which allows you to test the reliability of a single predicted instance made
             by your model and prediction function. It also allows you to make a correlation test to estimate which reliability estimate is the most 
             accurate for your model.
	"""
	
	cran = "predReliability" 

	version("0.1.0", md5="fb9865a5b54f3ee2853a68395a292af5")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
