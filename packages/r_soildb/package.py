# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoildb(RPackage):
	"""Soil Database Interface

	A collection of functions for reading soil data from U.S. Department of Agriculture Natural Resources Conservation Service (USDA-NRCS) and National Cooperative Soil Survey (NCSS) databases.
	"""
	
	homepage = "https://ncss-tech.github.io/soilDB/"
	cran = "soilDB" 

	version("2.8.1", md5="0abfc29a487fd063fdabc9855e28009d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-aqp@2.0.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
