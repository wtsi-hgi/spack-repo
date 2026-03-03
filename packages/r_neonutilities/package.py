# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeonutilities(RPackage):
	"""Utilities for Working with NEON Data

	NEON data packages can be accessed through the NEON Data Portal <https://www.neonscience.org>
    or through the NEON Data API (see <https://data.neonscience.org/data-api> for documentation). Data delivered from
    the Data Portal are provided as monthly zip files packaged within a parent zip file, while individual files
    can be accessed from the API. This package provides tools that aid in discovering, downloading, and reformatting 
    data prior to use in analyses. This includes downloading data via the API, merging data tables by type, and 
    converting formats. For more information, see the readme file at <https://github.com/NEONScience/NEON-utilities>.
	"""
	
	homepage = "https://github.com/NEONScience/NEON-utilities"
	cran = "neonUtilities" 

	version("2.4.1", md5="a127480073b00bd620babe2ac4b9403c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-downloader", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
