# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIe2misc(RPackage):
	"""Irucka Embry's Miscellaneous USGS Functions

	A collection of Irucka Embry's miscellaneous USGS functions
    (processing .exp and .psf files, statistical error functions,
    "+" dyadic operator for use with NA, creating ADAPS and QW
    spreadsheet files, calculating saturated enthalpy). Irucka created these
    functions while a Cherokee Nation Technology Solutions (CNTS) United States
    Geological Survey (USGS) Contractor and/or USGS employee.
	"""
	
	homepage = "https://gitlab.com/iembry/ie2misc"
	cran = "ie2misc" 

	version("0.9.1", md5="09fb1b44b401ab465d7ed32beb362107")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-readxl@1.3.1:", type=("build", "run"))
	depends_on("r-openxlsx@4.1.4:", type=("build", "run"))
	depends_on("r-gwidgets2", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-mgsub", type=("build", "run"))
	depends_on("r-reader", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-data-table@1.10.2:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
