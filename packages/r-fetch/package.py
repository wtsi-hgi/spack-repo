# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFetch(RPackage):
	"""Fetch Data from Various Data Sources

	Contains functions to fetch data from various data sources.
    The user first creates a catalog of objects from a data source,
    then fetches data from the catalog.  The package provides an easy
    way to access data from many different types of sources.
	"""
	
	homepage = "https://fetch.r-sassy.org"
	cran = "fetch" 

	version("0.1.5", md5="d4731bce6c9dd66a8f419043da90fa14")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-common", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
