# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCombineportfolio(RPackage):
	"""Estimation of Optimal Portfolio Weights by Combining Simple
Portfolio Strategies

	Estimation of optimal portfolio weights as combination of simple portfolio strategies, like the tangency, global minimum variance (GMV) or naive (1/N) portfolio. It is based on a utility maximizing 8-fund rule. Popular special cases like the Kan-Zhou(2007) 2-fund and 3-fund rule or the Tu-Zhou(2011) estimator are nested.
	"""
	
	cran = "CombinePortfolio" 

	version("0.4", md5="2aecea5f338bd4cbd05d0ee7c4dbabc8")

	depends_on("r@3.0.2:", type=("build", "run"))
