# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPenic(RPackage):
	"""Semiparametric Regression Analysis of Interval-Censored Data
using Penalized Splines

	Currently incorporate the generalized odds-rate model (a type of linear 
    transformation model) for interval-censored data based on penalized monotonic B-Spline. 
    More methods under other semiparametric models such as cure model or additive model will
    be included in future versions. For more details see Lu, M., Liu, Y., Li, C. and Sun, J. 
    (2019) <arXiv:1912.11703>.
	"""
	
	cran = "PenIC" 

	version("1.0.0", md5="44b825841d3991cab291f9055662f61d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
