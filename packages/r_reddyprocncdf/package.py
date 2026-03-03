# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReddyprocncdf(RPackage):
	"""Reading Data from NetCDF Files for 'REddyProc'

	Extension to 'REddyProc' that allows reading data from netCDF files.
	"""
	
	homepage = "https://github.com/bgctw/REddyProcNCDF"
	cran = "REddyProcNCDF" 

	version("1.1.4", md5="578f5802f8d13012a3a382fa3414a7fb")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-reddyproc", type=("build", "run"))
