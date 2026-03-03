# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKutils(RPackage):
	"""Project Management Tools

	Tools for data importation, recoding, and inspection.
    There are functions to create new project
    folders, R code templates, create uniquely named output
    directories, and to quickly obtain a visual summary for each
    variable in a data frame.  The main feature here is the systematic
    implementation of the "variable key" framework for data
    importation and recoding.  We are eager to have community feedback
    about the variable key and the vignette about it. In version 1.7,
    the function 'semTable' is removed. It was deprecated since 1.67.
    That is provided in a separate package, 'semTable'.
	"""
	
	cran = "kutils" 

	version("1.73", md5="d45336a7a638f6057cda6701b04fee2b")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-runit", type=("build", "run"))
