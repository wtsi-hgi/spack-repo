# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGtfsio(RPackage):
	"""Read and Write General Transit Feed Specification (GTFS) Files

	Tools for the development of packages related to General
    Transit Feed Specification (GTFS) files. Establishes a standard for
    representing GTFS feeds using R data types. Provides fast and flexible
    functions to read and write GTFS feeds while sticking to this
    standard. Defines a basic 'gtfs' class which is meant to be extended
    by packages that depend on it. And offers utility functions that
    support checking the structure of GTFS objects.
	"""
	
	homepage = "https://r-transit.github.io/gtfsio/"
	cran = "gtfsio" 

	version("1.1.1", md5="66810055f1a14ff1a2b71c541e3e15e7")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
