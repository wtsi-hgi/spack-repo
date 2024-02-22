# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSscor(RPackage):
	"""Robust Correlation Estimation and Testing Based on Spatial Signs

	Provides the spatial sign correlation and the two-stage spatial sign correlation as well as a one-sample test for the correlation coefficient.
	"""
	
	cran = "sscor" 

	version("0.2", md5="47995184a7cb8d19d8e97c28122345c9")

	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
