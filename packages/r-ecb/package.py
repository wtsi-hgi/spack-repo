# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcb(RPackage):
	"""Programmatic Access to the European Central Bank's Statistical
Data Warehouse

	Provides an interface to the 'European Central Bank's Statistical
    Data Warehouse' API <https://sdw.ecb.europa.eu/>, allowing for programmatic 
    retrieval of a vast quantity of statistical data.
	"""
	
	homepage = "https://sdw.ecb.europa.eu/"
	cran = "ecb" 

	version("0.4.2", md5="65cef10144214e3f577d65e1534a52e5")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-rsdmx", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
