# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrct(RPackage):
	"""Outlier Detection of Functional Data Based on the Minimum
Regularized Covariance Trace Estimator

	Detect outlying observations in functional data sets based on the minimum regularized covariance trace (MRCT) estimator. Includes implementation of Oguamalam et al. (2023) <arXiv:2307.13509>.
	"""
	
	cran = "mrct" 

	version("0.0.1.0", md5="728ee7c7ad5e3e85f2f347decd6e6ab6")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-fdapace", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
