# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynpanel(RPackage):
	"""Dynamic Panel Data Models

	Computes the first stage GMM estimate of a dynamic linear model with p lags of the dependent variables.
	"""
	
	cran = "dynpanel" 

	version("0.1.0", md5="4ecd0e014a7dd0526b237747608ce0cb")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
