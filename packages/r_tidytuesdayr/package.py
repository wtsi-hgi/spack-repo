# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidytuesdayr(RPackage):
	"""Access the Weekly 'TidyTuesday' Project Dataset

	
  'TidyTuesday' is a project by the 'R4DS Online Learning Community' in which they 
  post a weekly dataset onto post a weekly dataset in a public data repository 
  (<https://github.com/rfordatascience/tidytuesday>) for people to
  analyze and visualize. This package provides the tools to easily download this data and the 
  description of the source.
	"""
	
	homepage = "https://github.com/thebioengineer/tidytuesdayR"
	cran = "tidytuesdayR" 

	version("1.0.3", md5="4c23d56a197a7dd1b03292c533ea56d2")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-readxl@1:", type=("build", "run"))
	depends_on("r-rvest@0.3.2:", type=("build", "run"))
	depends_on("r-lubridate@1.7:", type=("build", "run"))
	depends_on("r-purrr@0.2.5:", type=("build", "run"))
	depends_on("r-readr@1:", type=("build", "run"))
	depends_on("r-rstudioapi@0.2:", type=("build", "run"))
	depends_on("r-xml2@1.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
