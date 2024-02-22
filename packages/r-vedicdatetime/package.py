# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVedicdatetime(RPackage):
	"""Vedic Calendar System

	Provides platform for Vedic calendar system having several
    functionalities to facilitate conversion between Gregorian and Vedic
    calendar systems, and helpful in examining its impact in the
    time series analysis domain.
	"""
	
	homepage = "https://www.neerajbokde.in/viggnette/2022-09-05-VedicDateTime"
	cran = "VedicDateTime" 

	version("0.1.9", md5="e13e293df348eb19b9973da17d9867ea")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-swephr", type=("build", "run"))
