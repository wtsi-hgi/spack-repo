# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsdmx(RPackage):
	"""Tools for Reading SDMX Data and Metadata

	Set of classes and methods to read data and metadata documents
  exchanged through the Statistical Data and Metadata Exchange (SDMX) framework,
  currently focusing on the SDMX XML standard format (SDMX-ML).
	"""
	
	homepage = "https://github.com/opensdmx/rsdmx"
	cran = "rsdmx" 

	version("0.6-3", md5="7ce9b4f6caab1cf78856c407536e7f30")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-xml@3.98.1.3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
