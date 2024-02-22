# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApproximator(RPackage):
	"""Bayesian Prediction of Complex Computer Codes

	Performs Bayesian prediction of complex computer codes when fast approximations are available.  It uses a hierarchical version of the Gaussian process, originally proposed by Kennedy and O'Hagan (2000), Biometrika 87(1):1.
	"""
	
	cran = "approximator" 

	version("1.2-8", md5="15002c96c05eedb2e41adf866c948ae7")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-emulator@1.2.11:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
