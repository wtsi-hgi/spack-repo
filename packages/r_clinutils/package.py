# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClinutils(RPackage):
	"""General Utility Functions for Analysis of Clinical Data

	
 Utility functions to facilitate the import, 
 the reporting and analysis of clinical data.
 Example datasets in 'SDTM' and 'ADaM' format, containing a subset of patients/domains
 from the 'CDISC Pilot 01 study' are also available as R datasets to demonstrate
 the package functionalities.
	"""
	
	homepage = "https://github.com/openanalytics/clinUtils"
	cran = "clinUtils" 

	version("0.1.4", md5="d3f996ae2f4733f83dfaf3dabef224f8")

	depends_on("r-crosstalk", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
