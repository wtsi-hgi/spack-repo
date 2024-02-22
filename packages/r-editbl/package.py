# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REditbl(RPackage):
	"""'DT' Extension for CRUD (Create, Read, Update, Delete)
Applications in 'shiny'

	The core of this package is a function eDT() which enhances DT::datatable() such that it can be used to interactively modify data in 'shiny'. By the use of generic 'dplyr' methods it supports many types of data storage, with relational databases ('dbplyr') being the main use case.
	"""
	
	homepage = "https://github.com/openanalytics/editbl"
	cran = "editbl" 

	version("1.0.3", md5="f37ab9714774351f291edadbcfd0bb2d")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-fontawesome@0.4:", type=("build", "run"))
