# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNhdplustools(RPackage):
	"""NHDPlus Tools

	Tools for traversing and working with National Hydrography Dataset Plus (NHDPlus) data. All methods implemented in 'nhdplusTools' are available in the NHDPlus documentation available from the US Environmental Protection Agency <https://www.epa.gov/waterdata/basic-information>.
	"""
	
	homepage = "https://doi-usgs.github.io/nhdplusTools/"
	cran = "nhdplusTools" 

	version("1.0.0", md5="4d75771bb4e496f86618a9c17f9ad2cb")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-hydroloom", type=("build", "run"))
	depends_on("r-dataretrieval", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-maptiles", type=("build", "run"))
	depends_on("r-mapsf", type=("build", "run"))
	depends_on("r-fst", type=("build", "run"))
	depends_on("r-arrow", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
