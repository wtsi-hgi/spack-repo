# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChoicedes(RPackage):
	"""Design Functions for Choice Studies

	Design functions for DCMs and other types of choice studies (including MaxDiff and other tradeoffs).
	"""
	
	cran = "choiceDes" 

	version("0.9-3", md5="48c01134e27c91a8f3d0b8176e677546")

	depends_on("r@2.15.2:", type=("build", "run"))
	depends_on("r-algdesign", type=("build", "run"))
