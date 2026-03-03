# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPocre(RPackage):
	"""Penalized Orthogonal-Components Regression

	Penalized orthogonal-components regression (POCRE) is a supervised dimension reduction method for high-dimensional data. It sequentially constructs orthogonal components (with selected features) which are maximally correlated to the response residuals. POCRE can also construct common components for multiple responses and thus build up latent-variable models.
	"""
	
	cran = "POCRE" 

	version("0.6.0", md5="40026a6b9b38a03c6e13c7ea15254a73")

	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-ebayesthresh", type=("build", "run"))
