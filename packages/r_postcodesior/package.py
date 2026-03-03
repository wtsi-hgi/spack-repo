# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPostcodesior(RPackage):
	"""API Wrapper Around 'Postcodes.io'

	Free UK geocoding using data from Office for National Statistics.
    It is using several functions to get information about post codes, outward
    codes, reverse geocoding, nearest post codes/outward codes, validation, or
    randomly generate a post code. API wrapper around <https://postcodes.io>.
	"""
	
	homepage = "https://docs.ropensci.org/PostcodesioR/"
	cran = "PostcodesioR" 

	version("0.3.1", md5="4a620e8a616c36448c34e64bd5c31177")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
