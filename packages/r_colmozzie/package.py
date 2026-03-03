# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColmozzie(RPackage):
	"""Dengue Cases and Climate Variables in Colombo Sri Lanka

	Weekly notified dengue cases and climate variables in Colombo district Sri Lanka from 2008/ week-52 to 2014/ week-21.
	"""
	
	cran = "colmozzie" 

	version("1.1.1", md5="5d01ed05a5d178123fdb9da37bf83e51")

	depends_on("r@2.10:", type=("build", "run"))
