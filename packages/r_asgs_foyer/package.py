# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsgsFoyer(RPackage):
	"""Interface to the Australian Statistical Geography Standard

	The Australian Statistical Geography Standard ('ASGS') is 
  a set of shapefiles by the Australian Bureau of Statistics. This package
  provides an interface to those shapefiles, as well as methods for converting
  coordinates to shapefiles.
	"""
	
	cran = "ASGS.foyer" 

	version("0.3.3", md5="29174b5f36e58cc028a2651a76af2c70")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
