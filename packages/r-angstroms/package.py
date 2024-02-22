# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAngstroms(RPackage):
	"""Tools for 'ROMS' the Regional Ocean Modeling System

	Helper functions for working with Regional Ocean Modeling System 'ROMS' output. See
    <https://www.myroms.org/> for more information about 'ROMS'. 
	"""
	
	homepage = "https://github.com/mdsumner/angstroms"
	cran = "angstroms" 

	version("0.0.1", md5="239edd7b7f6fc2012bc25ce6b3f4e69e")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-nabor", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-proj4", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spbabel", type=("build", "run"))
