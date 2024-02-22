# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSqlstrings(RPackage):
	"""Map 'SQL' Code to R Lists

	Provides a helper function, to bulk read 'SQL' code from separate files and load it into an 'R' list, where the list elements contain the individual statements and queries as strings. This works by annotating the 'SQL' code with a name comment, which also will be the name of the list element. 
	"""
	
	cran = "sqlstrings" 

	version("1.0.0", md5="c9a3850f3a7e6edb664ab576eacdca53")

	depends_on("r-fs", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
