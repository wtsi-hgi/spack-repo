# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCbinom(RPackage):
	"""Continuous Analog of a Binomial Distribution

	Implementation of the d/p/q/r family of functions for a continuous analog to the standard discrete binomial with continuous size parameter and continuous support with x in [0, size + 1], following Ilienko (2013) <arXiv:1303.5990>.
	"""
	
	cran = "cbinom" 

	version("1.6", md5="ebaccde1f6e13810c8832472a613816f")

	depends_on("r-rcpp", type=("build", "run"))
