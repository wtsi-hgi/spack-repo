# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClamr(RPackage):
	"""Time Series Modeling for Climate Change Proxies

	Implementation of the Wilkinson and Ivany (2002) approach to paleoclimate analysis, applied to isotope data extracted from clams.
	"""
	
	cran = "ClamR" 

	version("2.1-3", md5="af63eb29200bf316b052aa1b6e4b1fd5")

