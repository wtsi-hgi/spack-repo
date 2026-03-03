# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRadlibs(RPackage):
	"""Build Your Own Madlibs!

	Make your phrase or sentence into something funny! Pass a string with the keywords in, 
    and get out a bit of humor. 
	"""
	
	cran = "radlibs" 

	version("0.2.0", md5="147f16b9877103c767ef5c1a4bffb062")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lexicon", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
