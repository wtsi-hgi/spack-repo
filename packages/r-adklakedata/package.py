# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdklakedata(RPackage):
	"""Adirondack Long-Term Lake Data

	Package for the access and distribution of Long-term lake datasets from lakes in the 
    Adirondack Park, northern New York state. Includes a wide variety of physical, chemical, and 
    biological parameters from 28 lakes. Data are from multiple collection organizations and have 
    been harmonized in both time and space for ease of reuse. 
	"""
	
	cran = "adklakedata" 

	version("0.6.1", md5="8266ad494f1732eab063fc933401d5f1")

	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
