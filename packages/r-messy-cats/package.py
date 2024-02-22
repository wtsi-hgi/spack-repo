# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMessyCats(RPackage):
	"""Employs String Distance Tools to Help Clean Categorical Data

	Matching with string distance has never been easier! 'messy.cats' contains various functions that employ string distance tools in order to make data management easier for users working with categorical data. Categorical data, especially user inputted categorical data that often tends to be plagued by typos, can be difficult to work with. 'messy.cats' aims to provide functions that make cleaning categorical data simple and easy.  
	"""
	
	cran = "messy.cats" 

	version("1.0", md5="ef444ba23a2e917cedc1d27bf3eb2ffb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-varhandle", type=("build", "run"))
	depends_on("r-rapportools", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
