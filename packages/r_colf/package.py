# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColf(RPackage):
	"""Constrained Optimization on Linear Function

	Performs least squares constrained optimization on a linear objective function. It contains
    a number of algorithms to choose from and offers a formula syntax similar to lm().
	"""
	
	homepage = "https://github.com/LyzandeR/colf"
	cran = "colf" 

	version("0.1.3", md5="3a0c295167a3da2e73a6f36b29fd253f")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-nlsr", type=("build", "run"))
