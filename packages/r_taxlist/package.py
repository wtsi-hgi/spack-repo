# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTaxlist(RPackage):
	"""Handling Taxonomic Lists

	Handling taxonomic lists through objects of class 'taxlist'.
    This package provides functions to import species lists from 'Turboveg'
    (<https://www.synbiosys.alterra.nl/turboveg/>) and the possibility to create
    backups from resulting R-objects.
    Also quick displays are implemented as summary-methods.
	"""
	
	homepage = "https://cran.r-project.org/package=taxlist"
	cran = "taxlist" 

	version("0.2.4", md5="8f9c103dba88a0c481dc22fd8490f4b2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biblio@0.0.8:", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-vegdata", type=("build", "run"))
