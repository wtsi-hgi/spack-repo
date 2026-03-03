# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRslp(RPackage):
	"""A Stemming Algorithm for the Portuguese Language

	Implements the "Stemming Algorithm for the Portuguese Language" <DOI:10.1109/SPIRE.2001.10024>.
	"""
	
	homepage = "https://github.com/dfalbel/rslp"
	cran = "rslp" 

	version("0.2.0", md5="c559f3ab09b965c97c5929a1c2625157")

	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tokenizers", type=("build", "run"))
