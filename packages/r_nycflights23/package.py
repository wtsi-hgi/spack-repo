# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNycflights23(RPackage):
	"""Flights and Other Useful Metadata for NYC Outbound Flights in
2023

	Updating the now 10-year-old 'nycflights13' data package. It contains information about all flights that departed from the three main New York City airports in 2023 and metadata on airlines, airports, weather, and planes.
	"""
	
	homepage = "https://moderndive.github.io/nycflights23/"
	cran = "nycflights23" 

	version("0.1.0", md5="595c3a24d5b80522355edaaf4027fbf4", url="https://cran.r-project.org/src/contrib/nycflights23_0.1.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
