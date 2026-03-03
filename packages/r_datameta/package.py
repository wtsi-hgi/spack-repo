# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatameta(RPackage):
	"""Create and Append a Data Dictionary for an R Dataset

	Designed to create a basic data dictionary and append to the original dataset's attributes list. The package makes use of a tidy dataset and creates a data frame that will serve as a linker that will aid in building the dictionary. The dictionary is then appended to the list of the original dataset's attributes. The user will have the option of entering variable and item descriptions by writing code or use alternate functions that will prompt the user to add these.
	"""
	
	homepage = "https://github.com/dmrodz/dataMeta"
	cran = "dataMeta" 

	version("0.1.1", md5="aa898dbc7baa58a668738fd00905d726")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
