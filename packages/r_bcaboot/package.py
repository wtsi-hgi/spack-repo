# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcaboot(RPackage):
	"""Bias Corrected Bootstrap Confidence Intervals

	Computation of bootstrap confidence intervals in an almost automatic fashion as described in Efron and Narasimhan (2020, <doi:10.1080/10618600.2020.1714633>).
	"""
	
	homepage = "https://bnaras.github.io/bcaboot/"
	cran = "bcaboot" 

	version("0.2-3", md5="6f41c5857f96dbb34cec42d8b99fa55f")

	depends_on("r@3.5:", type=("build", "run"))
