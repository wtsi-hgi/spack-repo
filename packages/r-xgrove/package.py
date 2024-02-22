# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXgrove(RPackage):
	"""Explanation Groves

	Compute surrogate explanation groves for predictive machine learning models and analyze complexity vs. explanatory power of an explanation according to Szepannek, G. and von Holt, B. (2023) <doi:10.1007/s41237-023-00205-2>.
	"""
	
	cran = "xgrove" 

	version("0.1-7", md5="91f94d0024edcc120397b008974cc8d5")

	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))
