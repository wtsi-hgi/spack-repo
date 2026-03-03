# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFixedtimeevents(RPackage):
	"""The Distribution of Distances Between Discrete Events in Fixed
Time

	Distribution functions and test for over-representation of short
    distances in the Liland distribution. Simulation functions are included for
    comparison.
	"""
	
	homepage = "https://github.com/khliland/fixedTimeEvents/"
	cran = "fixedTimeEvents" 

	version("1.0.1", md5="9707e4584dd958a80fa5b7d4b5885bbe")

