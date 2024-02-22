# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUsmapdata(RPackage):
	"""Mapping Data for 'usmap' Package

	Provides a container for data used by the 'usmap' package.
    The data used by 'usmap' has been extracted into this package so that the
    file size of the 'usmap' package can be reduced greatly. The data in this
    package will be updated roughly once per year (plus bug fixes) as new
    shapefiles are provided by the US Census bureau.
	"""
	
	homepage = "https://usmap.dev"
	cran = "usmapdata" 

	version("0.2.1", md5="0b0853a0e0805ab6aa3e8eac91895ad0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
