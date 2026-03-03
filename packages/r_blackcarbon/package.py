# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlackcarbon(RPackage):
	"""Processing Raw Black Carbon Concentration

	The functions in this package are designed to be used in the processing of black carbon concentration collected by a specific type of a personal monitor. The package includes functions for processing of the data by applying Optimized noise reduction averaging algorithm along with filter loading correction and with an option of filter change adjustment.
	"""
	
	cran = "BlackCarbon" 

	version("0.1.0", md5="eef7e13e9c4d0cb735abe8ce58badbb6")

	depends_on("r@2.10:", type=("build", "run"))
