# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMasswater(RPackage):
	"""Quality Control and Analysis of Massachusetts Water Quality Data

	Methods for quality control and exploratory analysis of surface 
  water quality data collected in Massachusetts, USA.  Functions are developed 
  to facilitate data formatting for the Water Quality Exchange Network 
  <https://www.epa.gov/waterdata/water-quality-data-upload-wqx> and reporting 
  of data quality objectives to state agencies. Quality control methods are 
  from Massachusetts Department of Environmental Protection (2020) 
  <https://www.mass.gov/orgs/massachusetts-department-of-environmental-protection>.
	"""
	
	homepage = "<https://github.com/massbays-tech/MassWateR>"
	cran = "MassWateR" 

	version("2.1.4", md5="dd0d72d206c7ed029a8b25ef566354e6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggspatial", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-prettymapr", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
