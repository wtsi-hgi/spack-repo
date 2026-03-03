# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmmoniaconcentration(RPackage):
	"""Un-Ionized Ammonia Concentration

	Provides a function to calculate the concentration of un-ionized ammonia in the total ammonia in aqueous solution using the pH and temperature values.
	"""
	
	homepage = "https://github.com/tumenas/ammonia"
	cran = "AmmoniaConcentration" 

	version("0.1", md5="16f068aa617c91efe64b5fa578bea19a")

