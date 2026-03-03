# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcohydmod(RPackage):
	"""Ecohydrological Modelling

	Simulates the soil water balance (soil moisture, evapotranspiration, leakage and runoff), rainfall series by using the marked Poisson process and the vegetation growth through the normalized difference vegetation index (NDVI). Please see Souza et al. (2016) <doi:10.1002/hyp.10953>.
	"""
	
	cran = "Ecohydmod" 

	version("1.0.0", md5="1fd0414065f904101c6bd5a08beaf257")

