# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDataspice(RPackage):
	"""Create Lightweight Schema.org Descriptions of Data

	The goal of 'dataspice' is to make it easier for researchers to
  create basic, lightweight, and concise metadata files for their datasets.
  These basic files can then be used to make useful information available during
  analysis, create a helpful dataset "README" webpage, and produce more complex
  metadata formats to aid dataset discovery. Metadata fields are based on
  the 'Schema.org' and 'Ecological Metadata Language' standards.
	"""
	
	homepage = "https://github.com/ropensci/dataspice"
	cran = "dataspice" 

	version("1.1.0", md5="d553b18a48f519348f1edc2aa1091c19")

	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-eml", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rhandsontable", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
