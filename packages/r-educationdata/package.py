# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REducationdata(RPackage):
	"""Retrieve Records from the Urban Institute's Education Data
Portal API

	Allows R users to retrieve and parse data from the Urban 
    Institute's Education Data API <https://educationdata.urban.org/> into a 
    'data.frame' for analysis.
	"""
	
	homepage = "https://urbaninstitute.github.io/education-data-package-r/"
	cran = "educationdata" 

	version("0.1.3", md5="344ab36efc292b53295ca247d0f640a9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
