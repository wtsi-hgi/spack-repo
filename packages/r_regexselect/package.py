# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegexselect(RPackage):
	"""Regular Expressions in 'shiny' Select Lists

	'shiny' extension that adds regular expression filtering capabilities to 
  the choice vector of the select list.
	"""
	
	homepage = "https://github.com/yonicd/regexSelect"
	cran = "regexSelect" 

	version("1.0.0", md5="809812677d961245acab7d396d70c40d")

	depends_on("r@2.3:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
