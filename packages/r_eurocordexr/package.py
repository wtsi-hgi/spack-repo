# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REurocordexr(RPackage):
	"""Makes it Easier to Work with Daily 'netCDF' from EURO-CORDEX
RCMs

	
    Daily 'netCDF' data from e.g. regional climate models (RCMs) are not trivial
    to work with. This package, which relies on 'data.table', makes it easier
    to deal with large data from RCMs, such as from EURO-CORDEX 
    (<https://www.euro-cordex.net/>, <https://cordex.org/data-access/>). It has 
    functions to extract single grid cells from rotated pole grids as well as 
    the whole array in long format. Can handle non-standard calendars (360, 
    noleap) and interpolate them to a standard one. Potentially works with many 
    CF-conform 'netCDF' files. 
	"""
	
	homepage = "https://github.com/mitmat/eurocordexr"
	cran = "eurocordexr" 

	version("0.2.4", md5="55206ef7b91604ac2bb85bd812aef87c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-ncdf4-helpers", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-pcict", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
