# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGogarch(RPackage):
	"""Generalized Orthogonal GARCH (GO-GARCH) Models

	Provision of classes and methods for estimating generalized
   orthogonal GARCH models. This is an alternative approach to CC-GARCH models
   in the context of multivariate volatility modeling.
	"""
	
	cran = "gogarch" 

	version("0.7-5", md5="4d9218f318013002ddc63ba4f010001a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fgarch", type=("build", "run"))
	depends_on("r-fastica", type=("build", "run"))
