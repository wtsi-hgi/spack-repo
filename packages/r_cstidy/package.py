# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCstidy(RPackage):
	"""Helpful Functions for Cleaning Surveillance Data

	Helpful functions for the cleaning and manipulation of surveillance data, especially with regards to the creation and validation of panel data from individual level surveillance data.
	"""
	
	homepage = "https://www.csids.no/cstidy/"
	cran = "cstidy" 

	version("2023.5.24", md5="c94310bb1088e576fe95cc4de68fedda")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-csdata", type=("build", "run"))
	depends_on("r-cstime", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
