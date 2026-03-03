# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKingcountyhouses(RPackage):
	"""Data on House Sales in King County WA

	Data on houses in and around Seattle WA are included. Basic 
    characteristics are given along with sale prices. 
	"""
	
	cran = "KingCountyHouses" 

	version("0.1.0", md5="20522f53a039b2b16fdcd1ad9c5ba55a")

	depends_on("r@2.10:", type=("build", "run"))
