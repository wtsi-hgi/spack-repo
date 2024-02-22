# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNycflights13(RPackage):
	"""Flights that Departed NYC in 2013

	Airline on-time data for all flights departing NYC in 2013.
    Also includes useful 'metadata' on airlines, airports, weather, and
    planes.
	"""
	
	homepage = "https://github.com/hadley/nycflights13"
	cran = "nycflights13" 

	version("1.0.2", md5="3d483829c9d11c675044cbe7cdf79f3a", url="https://cran.r-project.org/src/contrib/nycflights13_1.0.2.tar.gz")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
