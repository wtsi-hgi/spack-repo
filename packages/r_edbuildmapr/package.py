# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdbuildmapr(RPackage):
	"""Download School District Geospatial Data, Perform Spatial
Analysis, and Create Formatted Exportable Maps

	Import US Census Bureau, Education Demographic and Geographic Estimates Program,
  Composite School District Boundaries Files for 2013-2019 with the option to attach the 'EdBuild'
  master dataset of school district finance, student demographics, and community economic
  indicators for every school district in the United States. The master dataset is built
  from the US Census, Annual Survey of School System Finances (F33) and joins data from the
  National Center for Education Statistics, Common Core of Data; the US Census, Small Area
  Income and Poverty Estimates; and the US Census, Education Demographic and Geographic
  Estimates. Additional functions in the package create a dataset of all pairs of school
  district neighbors as either a dataframe or a shapefile and create formatted maps of
  selected districts at the state or neighbor level, symbolized by a selected variable
  in the 'EdBuild' master dataset. For full details about 'EdBuild' data processing please
  see 'EdBuild' (2020) <http://data.edbuild.org/>. 
	"""
	
	homepage = "https://github.com/EdBuild/edbuildmapr"
	cran = "edbuildmapr" 

	version("0.3.1", md5="b5fb3358f0f3fd934f18e8d10e467009")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-sf@0.9.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
	depends_on("r-tmap@3:", type=("build", "run"))
