# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKsd(RPackage):
	"""Goodness-of-Fit Tests using Kernelized Stein Discrepancy

	An adaptation of Kernelized Stein Discrepancy, this package provides a goodness-of-fit test of whether a given i.i.d. sample is drawn from a given distribution. It works for any distribution once its score function (the derivative of log-density) can be provided. This method is based on "A Kernelized Stein Discrepancy for Goodness-of-fit Tests and Model Evaluation" by Liu, Lee, and Jordan, available at <arXiv:1602.03253>.
	"""
	
	cran = "KSD" 

	version("1.0.1", md5="5fadb24087173e26d387f93a957b9a6c")

	depends_on("r-pryr", type=("build", "run"))
