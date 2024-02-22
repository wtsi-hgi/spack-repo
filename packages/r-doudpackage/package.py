# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoudpackage(RPackage):
	"""Create Elegant Table 1 in HTML for Bio-Statistics

	Creates the "table one" of bio-medical papers. Fill it with your data and the name of the variable which you'll make the group(s) out of and it will make univariate, bivariate analysis and parse it into HTML.
    It also allows you to visualize all your data with graphic representation.
	"""
	
	cran = "doudpackage" 

	version("2.1.0", md5="8645608d66f1ad566fa9290d58d6f985")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
