# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBmamevt(RPackage):
	"""Multivariate Extremes: Bayesian Estimation of the Spectral
Measure

	Toolkit for Bayesian estimation of the dependence structure in multivariate extreme value parametric models, following Sabourin and Naveau (2014) <doi:10.1016/j.csda.2013.04.021> and Sabourin, Naveau and Fougeres (2013) <doi:10.1007/s10687-012-0163-0>.
	"""
	
	cran = "BMAmevt" 

	version("1.0.5", md5="eaec386343b24b63d1cd1fd819d1e68a")

	depends_on("r-coda", type=("build", "run"))
