# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSorcering(RPackage):
	"""Soil Organic Carbon and CN Ratio Driven Nitrogen Modelling
Framework

	Can be used to model the fate of soil organic carbon and soil organic nitrogen and to calculate N mineralisation rates. Provides a framework that numerically solves differential equations of soil organic carbon models based on first-order kinetics and extends these models to include the nitrogen component. The name 'sorcering' is an acronym for 'Soil ORganic Carbon & CN Ratio drIven Nitrogen modellinG framework'.
	"""
	
	cran = "sorcering" 

	version("1.0.0.1", md5="59fd4008add61fae34d01d6732abc598")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
