# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodaimpact(RPackage):
	"""Interpreting CoDa Regression Models

	
    Provides methods for interpreting CoDa (Compositional Data) regression models along the lines of "Pairwise share ratio interpretations of compositional regression models" (Dargel and Thomas-Agnan 2024) <doi:10.1016/j.csda.2024.107945>.
    The new methods include variation scenarios, elasticities, elasticity differences and share ratio elasticities.
    These tools are independent of log-ratio transformations and allow an interpretation in the original space of shares.
    'CoDaImpact' is designed to be used with the 'compositions' package and its ecosystem.
	"""
	
	homepage = "https://github.com/LukeCe/CoDaImpact"
	cran = "CoDaImpact" 

	version("0.1.0", md5="92fd7d3b5adf4e8c80f27d4159e44fee")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-compositions", type=("build", "run"))
