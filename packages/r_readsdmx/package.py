# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadsdmx(RPackage):
	"""Read SDMX-XML Data

	Read Statistical Data and Metadata Exchange (SDMX) XML data. 
    This the main transmission format used in official statistics. Data can be imported from
    local SDMX-ML files or a SDMX web-service and will be read in 'as is' into a dataframe object.
    The 'RapidXML' C++ library <https://rapidxml.sourceforge.net/> is used to parse the XML data.
	"""
	
	homepage = "https://github.com/mdequeljoe/readsdmx"
	cran = "readsdmx" 

	version("0.3.1", md5="f9d93b97fc4cad7ff40c39707ec5adbe")

	depends_on("r-rcpp", type=("build", "run"))
