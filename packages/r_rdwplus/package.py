# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdwplus(RPackage):
	"""An Implementation of IDW-PLUS

	Compute spatially explicit land-use metrics for stream survey sites in GRASS GIS and R as an open-source implementation of IDW-PLUS (Inverse Distance Weighted Percent Land Use for Streams). The package includes functions for preprocessing digital elevation and streams data, and one function to compute all the spatially explicit land use metrics described in Peterson et al. (2011) <doi:10.1111/j.1365-2427.2010.02507.x> and previously implemented by Peterson and Pearse (2017) <doi:10.1111/1752-1688.12558> in ArcGIS-Python as IDW-PLUS. 
	"""
	
	cran = "rdwplus" 

	version("1.0.0", md5="513b030ef57cb6fb5c493ede20e67726")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rgrass", type=("build", "run"))
	depends_on("r-stars", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
