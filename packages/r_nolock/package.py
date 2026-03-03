# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNolock(RPackage):
	"""Append 'WITH (NOLOCK)' to 'SQL' Queries, Get Packages in Active
Script

	Provides a suite of tools that can assist in enhancing the 
    processing efficiency of 'SQL' and 'R' scripts. 
    - The 'libr_unused()' retrieves a vector of package names that are called 
    within an 'R' script but are never actually used in the script.
    - The 'libr_used()' retrieves a vector of package names actively utilized 
    within an 'R' script; packages loaded using 'library()' but not actually 
    used in the script will not be included.
    - The 'libr_called()' retrieves a vector of all package names which are 
    called within an 'R' script.
    - 'nolock()' appends 'WITH (nolock)' to all tables in 'SQL' queries. This 
    facilitates reading from databases in scenarios where non-blocking reads are 
    preferable, such as in high-transaction environments.
	"""
	
	cran = "nolock" 

	version("1.1.0", md5="e288f15baaace5e0b94807ebe62c1404")

	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ncmisc", type=("build", "run"))
