# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RObservation(RPackage):
	"""Collect and Process Physical Activity Direct Observation Data

	Two-part system for first collecting then managing direct
    observation data, as described by Hibbing PR, Ellingson LD,
    Dixon PM, & Welk GJ (2018) <doi:10.1249/MSS.0000000000001486>.
	"""
	
	homepage = "https://github.com/paulhibbing/Observation"
	cran = "Observation" 

	version("0.3.0", md5="c8fca735f8aef3347980607378d2c1a0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-svdialogs@1:", type=("build", "run"))
