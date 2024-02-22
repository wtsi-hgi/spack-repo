# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDacf(RPackage):
	"""Data Analysis with Ceiling and/or Floor Data

	An implementation of data analytic methods in R for analyses for data with ceiling/floor effects. The package currently includes functions for mean/variance estimation and mean comparison tests. Implemented methods are from Aitkin (1964) <doi:10.1007/BF02289723> and Liu & Wang (in prep).
	"""
	
	cran = "DACF" 

	version("1.0.0", md5="084c189e89d6ac23bbdc96fa1e504344")

