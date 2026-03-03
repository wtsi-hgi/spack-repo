# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNonmemica(RPackage):
	"""Create and Evaluate NONMEM Models in a Project Context

	Systematically creates and modifies NONMEM(R) control streams. Harvests
 NONMEM output, builds run logs, creates derivative data, generates diagnostics.
 NONMEM (ICON Development Solutions <https://www.iconplc.com/>) is software for 
 nonlinear mixed effects modeling. See 'package?nonmemica'. 
	"""
	
	cran = "nonmemica" 

	version("1.0.8", md5="80ce1704943e62c54db0e002af6316da")

	depends_on("r-dplyr@0.7.1:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-encode", type=("build", "run"))
	depends_on("r-csv", type=("build", "run"))
	depends_on("r-spec", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-metaplot@0.1.4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
