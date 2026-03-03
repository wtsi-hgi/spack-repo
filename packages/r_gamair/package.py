# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamair(RPackage):
	"""Data for 'GAMs: An Introduction with R'

	Data sets and scripts used in the book 'Generalized Additive 
             Models: An Introduction with R', Wood (2006,2017) CRC.
	"""
	
	cran = "gamair" 

	version("1.0-2", md5="0d98aac0258150f5d17acc12ccb8ca3a")

	depends_on("r@2.10:", type=("build", "run"))
