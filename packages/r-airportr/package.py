# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAirportr(RPackage):
	"""Convenience Tools for Working with Airport Data

	Retrieves open source airport data and provides tools to look up information, translate names into codes and vice-verse, as well as some basic calculation functions for measuring distances. Data is licensed under the Open Database License. 
	"""
	
	homepage = "https://github.com/dshkol/airportr"
	cran = "airportr" 

	version("0.1.3", md5="4b46469fbd17c0b4a26f84cbd1be650d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
