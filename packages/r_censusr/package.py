# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCensusr(RPackage):
	"""Collect Data from the Census API

	Use the US Census API to collect summary data tables
    for SF1 and ACS datasets at arbitrary geographies.
	"""
	
	homepage = "https://github.com/transportfoundry/censusr"
	cran = "censusr" 

	version("0.0.4", md5="509a8b3f8b9e02acdebc7d7d7f68be39")

	depends_on("r-dplyr@0.4.3:", type=("build", "run"))
	depends_on("r-httr@1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
