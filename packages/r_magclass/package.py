# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMagclass(RPackage):
	"""Data Class and Tools for Handling Spatial-Temporal Data

	Data class for increased interoperability working with
    spatial-temporal data together with corresponding functions and
    methods (conversions, basic calculations and basic data manipulation).
    The class distinguishes between spatial, temporal and other dimensions
    to facilitate the development and interoperability of tools build for
    it. Additional features are name-based addressing of data and internal
    consistency checks (e.g. checking for the right data order in
    calculations).
	"""
	
	homepage = "https://github.com/pik-piam/magclass"
	cran = "magclass" 

	version("6.13.2", md5="7fd8dfe758453512e21df9a4091048c1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
