# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHydroloom(RPackage):
	"""Utilities to Weave Hydrologic Fabrics

	A collection of utilities that support creation of network attributes for hydrologic networks. Methods and algorithms implemented are documented in Moore et al. (2019) <doi:10.3133/ofr20191096>), Cormen and Leiserson (2022) <ISBN:9780262046305> and Verdin and Verdin (1999) <doi:10.1016/S0022-1694(99)00011-6>.  
	"""
	
	homepage = "https://github.com/DOI-USGS/hydroloom"
	cran = "hydroloom" 

	version("1.0.2", md5="05ea5f4c2949471eff39cd8e76220825")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-fastmap", type=("build", "run"))
