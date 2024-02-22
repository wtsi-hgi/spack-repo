# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSolarpos(RPackage):
	"""Solar Position Algorithm for Solar Radiation Applications

	Calculation of solar zenith and azimuth angles.
	"""
	
	cran = "solarPos" 

	version("1.0", md5="69db527dc9343bf42f2766021454fbb7")

