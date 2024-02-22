# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetda(RPackage):
	"""Network-Based Discriminant Analysis Subject to Multi-Label
Classes

	Implementation of discriminant analysis with network structures in predictors accommodated to do classification and prediction.
	"""
	
	cran = "NetDA" 

	version("0.2.0", md5="6e3ff773275c360707aa4baeacab276e")

	depends_on("r-glasso", type=("build", "run"))
