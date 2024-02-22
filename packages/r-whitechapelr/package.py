# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWhitechapelr(RPackage):
	"""Advanced Policing Techniques for the Board Game "Letters from
Whitechapel"

	Provides a set of functions to make tracking the hidden movements 
  of the 'Jack' player easier. By tracking every possible path Jack might have 
  traveled from the point of the initial murder including special movement such 
  as through alleyways and via carriages, the police can more accurately narrow 
  the field of their search. Additionally, by tracking all possible hideouts from 
  round to round, rounds 3 and 4 should have a vastly reduced field of search.
	"""
	
	cran = "whitechapelR" 

	version("0.3.0", md5="9cb6acea18cf3a4452a5f0e22bfe4c21")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
