# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmp(RPackage):
	"""Rounded Mixture Package

	Performs univariate probability mass function estimation via Bayesian nonparametric mixtures of rounded kernels as in Canale and Dunson (2011) <doi:10.1198/jasa.2011.tm10552>.
	"""
	
	cran = "rmp" 

	version("2.2", md5="5c6c073fd6c0d4666db87b2fb242d03e")

