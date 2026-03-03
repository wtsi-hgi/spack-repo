# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbwebforms(RPackage):
	"""Produce R Functions to Create HTML Forms Based on SQL Meta Data

	Offers meta programming style tools to generate configurable R functions that produce HTML forms based on table input and SQL meta data. 
    Also generates functions for collecting the parameters of those HTML forms after they are submitted. Useful for 
    quickly generating HTML forms based on existing SQL tables. To use the resultant functions, the output files containing those functions must 
    be read into the R environment (perhaps using base::source()).
	"""
	
	cran = "dbWebForms" 

	version("0.1.0", md5="d6f259e68dec20eb7ea88f72de17df27")

	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-html5", type=("build", "run"))
