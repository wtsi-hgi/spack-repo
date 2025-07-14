# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REstrogen(RPackage):
	"""Microarray dataset that can be used as example for 2x2 factorial designs

	Data from 8 Affymetrix genechips, looking at a 2x2 factorial design (with 2 repeats per level).
	"""
	
	bioc = "estrogen"

	version("1.54.0", commit="266ae624dbd4a8a1aef563c9691255b005c04108")
	version("1.48.0", commit="9e8a694929608ef8e930bcde839b370eed175099")


