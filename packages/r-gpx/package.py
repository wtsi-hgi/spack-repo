# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpx(RPackage):
	"""Process GPX Files into R Data Structures

	Process open standard GPX files into data.frames for further use and analysis in R.
	"""
	
	cran = "gpx" 

	version("1.1.0", md5="ddd6fd880e3025bc7cdc95e4ae733872")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
