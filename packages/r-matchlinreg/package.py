# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatchlinreg(RPackage):
	"""Combining Matching and Linear Regression for Causal Inference

	Core functions as well as diagnostic and calibration tools for combining matching and linear regression for causal inference in observational studies.
	"""
	
	cran = "MatchLinReg" 

	version("0.8.1", md5="01de44857ed90a8ddb58f7495e7f916a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-matching", type=("build", "run"))
