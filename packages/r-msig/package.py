# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsig(RPackage):
	"""An R Package for Exploring Molecular Signatures Database

	The Molecular Signatures Database ('MSigDB') is one of the most widely 
    used and comprehensive databases of gene sets for performing gene set 
    enrichment analysis <doi:10.1016/j.cels.2015.12.004>. The 'msig' package provides 
    you with powerful, easy-to-use and flexible query functions for the 'MsigDB' 
    database.
        There are 2 query modes in the 'msig' package: online query and local query. 
    Both queries contain 2 steps: gene set name and gene.
        The online search is divided into 2 modes: registered search and 
    non-registered browse. For registered search, email that you registered should 
    be provided.
        Local queries can be made from local database, which can be updated by msig_update() function.
	"""
	
	cran = "msig" 

	version("1.0", md5="6341de798afff3b4f4f53d1ec4cf446c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-do", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-set", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-tmcn", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
