# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpsiwal(RPackage):
	"""Exact Post Selection Inference with Applications to the Lasso

	Implements the conditional estimation procedure of
  Lee, Sun, Sun and Taylor (2016) <doi:10.1214/15-AOS1371>.
  This procedure allows hypothesis testing on the mean of
  a normal random vector subject to linear constraints.
	"""
	
	homepage = "https://github.com/shabbychef/epsiwal"
	cran = "epsiwal" 

	version("0.1.0", md5="e65604039a85ee28efcb4044750babb0")

	depends_on("r@3.0.2:", type=("build", "run"))
