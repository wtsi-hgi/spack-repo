# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnivrng(RPackage):
	"""Univariate Pseudo-Random Number Generation

	Pseudo-random number generation of 17 univariate distributions proposed by Demirtas. (2005) <DOI:10.22237/jmasm/1114907220>.
	"""
	
	cran = "UnivRNG" 

	version("1.2.3", md5="f4b7a70c4b9954588514c7083fe9dbaf")

