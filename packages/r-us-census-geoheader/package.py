# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUsCensusGeoheader(RPackage):
	"""US 2010 Census SF2 Geographic Header Summary Levels 010-050

	A simple interface to the Geographic Header information
  from the "2010 US Census Summary File 2".  The entire Summary File 2
  is described at
  <https://catalog.data.gov/dataset/census-2000-summary-file-2-sf2>,
  but note that this package only provides access to parts of the
  geographic header ('geoheader') of the file.  In particular, only
  the first 101 columns of the geoheader are included and, more
  importantly, only rows with summary levels (SUMLEVs) 010 through 050
  (nation down through county level) are included.  In addition to
  access to (part of) the geoheader, the package also provides a
  decode function that takes a column name and value and, for certain
  columns, returns "the meaning" of that column (i.e., a "SUMLEV"
  value of 40 means "State"); without a value, the decode function
  attempts to describe the column itself.
	"""
	
	homepage = "https://gitlab.com/minshall/us-census-geoheader"
	cran = "us.census.geoheader" 

	version("1.0.2", md5="10f70a2fe21800c0a23e543368c50a3a")

	depends_on("r-tibble", type=("build", "run"))
