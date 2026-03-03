# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQst(RPackage):
	"""Store Tables in SQL Database

	Provides functions for quickly writing (and 
  reading back) a data.frame to file in 'SQLite' format. The name 
  stands for *Store Tables using 'SQLite'*, or alternatively for *Quick 
  Store Tables* (either way, it could be pronounced as *Quest*). 
  For data.frames containing the supported data 
  types it is intended to work as a drop-in replacement for the 
  'write_*()' and 'read_*()' functions provided by similar packages. 
	"""
	
	cran = "qst" 

	version("0.1.2", md5="ede7768f887544a0eee9bc1dfe8ae4fc")

	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dbplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
