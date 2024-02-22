# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcroname(RPackage):
	"""Engine for Acronyms and Initialisms

	A tool for generating acronyms and initialisms from arbitrary text input.
	"""
	
	cran = "acroname" 

	version("0.1.0", md5="d9db33762370cd14e163d9de65968a3d")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-hunspell", type=("build", "run"))
