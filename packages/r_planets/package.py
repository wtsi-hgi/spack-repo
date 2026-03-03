# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlanets(RPackage):
	"""Simple and Accessible Data from all Known Planets

	The goal of 'planets' is to provide of very simple and accessible data containing basic information from all known planets.
	"""
	
	cran = "planets" 

	version("0.1.0", md5="37cd399d3c2a8bd8e93c7e6c36786654")

	depends_on("r@2.10:", type=("build", "run"))
