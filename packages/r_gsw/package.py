# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsw(RPackage):
	"""Gibbs Sea Water Functions

	Provides an interface to the Gibbs 'SeaWater' ('TEOS-10') C library, version 3.06-16-0 (commit '657216dd4f5ea079b5f0e021a4163e2d26893371', dated 2022-10-11, available at <https://github.com/TEOS-10/GSW-C>, which stems from 'Matlab' and other code written by members of Working Group 127 of 'SCOR'/'IAPSO' (Scientific Committee on Oceanic Research / International Association for the Physical Sciences of the Oceans).
	"""
	
	homepage = "http://teos-10.github.io/GSW-R/"
	cran = "gsw" 

	version("1.1-1", md5="db567f68fe82443055255ee12a047421")

	depends_on("r@3.5:", type=("build", "run"))
