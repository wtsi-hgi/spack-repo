# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColorr(RPackage):
	"""Color Palettes for EPL, MLB, NBA, NHL, and NFL Teams

	Color palettes for EPL, MLB, NBA, NHL, and NFL teams.
	"""
	
	cran = "colorr" 

	version("1.0.0", md5="6f71aca61cc256dd0ae16af40a144a5d")

