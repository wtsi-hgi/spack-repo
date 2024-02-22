# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REventinterval(RPackage):
	"""Sequential Event Interval Analysis

	Functions for analysis of rate changes in sequential events.
	"""
	
	cran = "eventInterval" 

	version("1.3", md5="b03b6c47f7047489a11e328c6fd7791c")

	depends_on("r-mass", type=("build", "run"))
